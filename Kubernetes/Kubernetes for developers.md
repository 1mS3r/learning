
# Kubernetes for developers - Summary from course LDF259

## Objetives

- Containerize and deploy a new Python script​
- Configure the deployment with ConfigMaps, Secrets, and - SecurityContexts
- Understand multi-container Pod design
- Configure probes for Pod health
- Update and roll back an application
- Implement services and NetworkPolicies
- Use PersistentVolumeClaims for state persistence

## Kubernetes Architecture

Kubernetes is:

> an open-source system for automating deployment, scaling, and management of containerized applications

In its simplest form, Kubernetes is made of one or more central managers (aka masters) and worker nodes. The manager runs an API server, a scheduler, various operators and a datastore to keep the state of the cluster, container settings, and the networking configuration.

![Kubernetes Architecture Diagram](img/architecture-diagram.png)

Kubernetes exposes an API via the API server: you can communicate with the API using a local client called kubectl. The kube-scheduler sees the API requests for running a new container and finds a suitable node to run that container. Each node in the cluster runs two components: kubelet and kube-proxy. The kubelet systemd service receives spec information for container configuration, downloads and manages any necessary resources and works with the container engine on the local node to ensure the container runs or is restarted upon failure. The kube-proxy pod creates and manages local firewall rules and networking configuration to expose containers on the network.

