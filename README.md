# Port Scanner Project

This project implements a simple port scanner in Python, capable of scanning both TCP and UDP ports.

## How to Run

### Using Docker

1. Clone the repository:
    ```bash
    git clone git@github.com:yourusername/your-repo.git
    cd your-repo
    ```

2. Build the Docker image:
    ```bash
    docker build -t port-scanner .
    ```

3. Run the Docker container:
    ```bash
    docker run -it port-scanner
    ```

4. The script will ask for a target IP, port range, and protocol (TCP/UDP) to scan.

