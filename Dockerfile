# Base OS (Host)
FROM ubuntu:20.10 AS base

# Verify that all packages are up-to-date
RUN apt update -y --fix-missing

# In our host OS
FROM base AS builder

# Compile the source code
RUN apt update -y --fix-missing
RUN apt -y install clang-11 lldb-11 lld-11
RUN apt -y install clang
RUN apt -y install util-linux wget
RUN apt -y install unzip make

# Download the CarlSAT git repo:
RUN wget https://github.com/JBontes/CarlSAT_2021/archive/refs/heads/main.zip
RUN ls main.zip | xargs -n1 unzip

# A bit of cleanup
RUN rm *.zip

# Compile the source
WORKDIR /CarlSAT_2021-main/
RUN make clean && make

# Fork a new image from the base...
FROM base AS exec
# Add the CarlSAT program
COPY --from=builder /CarlSAT_2021-main/CarlSAT .
COPY --from=builder /CarlSAT_2021-main/*.wcard .

# Install python and pip
RUN apt -y install python3
RUN apt -y install python3-pip

# Copy requirements from project directory and install dependencies
COPY ./requirements.txt /
RUN pip3 install --no-cache-dir -r requirements.txt
RUN rm *.txt

# Install MySQL
RUN apt -y install mysql-server

# Assign a home directory for MySQL
RUN usermod -d /var/lib/mysql/ mysql

# Start MySQL and create database "CarlSAT_DB"
RUN service mysql start && mysqladmin create CarlSAT_DB 

# Copy project source files and dependency list to container
COPY ./src/*.py /
COPY ./configurations/* /
COPY ./test /

#Create user 'CarlSAT' and grant privileges
RUN service mysql start && mysql --user=root --skip-password CarlSAT_DB < create_user_config

# Run the experiment and copy the log file to the host
# | tee output.log && cp output.log /host/output.log
#CMD python3 ./carlsat_cli.py test1.wcard test-30