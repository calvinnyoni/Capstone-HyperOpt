# CSC3003S 2021 - Capstone Project
## Hyperparameter Optimisation
#### CarlSAT - a local search solver for MaxSAT with cardinality support

To run program, you need to first run the Docker engine. Thereafter from your project root, run the commands

```bash
docker build -t carlsat .
docker run carlsat
```

This will build out your Docker container and run your wrapper program in your container whilst also printing to stdout and redirecting IO to a log file.