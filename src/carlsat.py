import shlex
import subprocess
import helper


def run_carlsat(filename, timeout, args):
    """
    Create a subprocess pipe to call create a shell subprocess, run the CarlSAT program, and read the
    output written to the shell by the program.
    :return: returns output from the CarlSAT program to be logged and fed to the optimisation algorithm
    """
    command = './CarlSAT -a %i -b %i -c %i -e %i -f %i -r %i -x %i -t %i -v %i -z %s' \
              % (args[0], args[1], args[2], round(args[3], 0), round(args[4], 0), args[5], args[6], timeout, args[8],
                 filename)
    helper.inform("Running: %s" % command[2:])

    carlsat_output = subprocess.run([command],
                                    shell=True,
                                    capture_output=True,
                                    encoding='utf-8'
                                    )
    std_out = (carlsat_output.stdout.strip()).split("\n")

    if carlsat_output.returncode != 0 or len(std_out) <= 0:
        helper.raise_exception(carlsat_output.stderr)

    helper.inform(carlsat_output.stdout.strip())

    return get_cost(std_out)


def get_cost(console_output):
    time = float((console_output[-1].split())[-2])
    score = float((console_output[-2].split())[-1])

    return score + time
