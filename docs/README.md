# Documentation

This page provides an overview of Ansible, the project structure and the components deployed.

## Ansible Overview

[Ansible](https://www.ansible.com/overview/how-ansible-works) models your IT infrastructure by describing how all of your systems inter-relate, rather than just managing one system at a time.

It doesn't use any agents nor additional custom security infrastructure, so it's easy to deploy - and most importantly, it uses a very simple language, YAML, in the form of Ansible Playbooks that allow you to describe your automation jobs in a way that approaches plain English.

An Ansible playbook contains one or more roles. A role is an independent component which allows reuse of common configuration steps. It consists of a set of tasks used to configure a host to serve a certain purpose, for example, configuring a service. This is depicted in the diagram below.

![Playbook Ovewview](./resources/playbook-overview.png)

Roles are defined using YAML files with a predefined directory structure.

A role directory structure contains directories: defaults, vars, tasks, files, templates, meta, and handlers.

* **defaults** contains default variables for the role. Variables in defaults have the lowest priority so they are easy to override
* **vars** contains variables for the role. Variables in vars have higher priority than variables in the defaults directory
* **tasks** contains the main list of steps to be executed by the role
* **files** contains files which we want to be copied to the remote host. We don’t need to specify a path of resources stored in this directory
* **templates** contains file templates which support modifications from the role. We use the Jinja2 templating language for creating templates
* **meta** contains metadata of the role like an author, support platforms, and dependencies
* **handlers** contains handlers which can be invoked by “notify” directives and are associated with a service

## Project Overview

The project contains a playbook and multiple roles.

The ACS playbook can be found in the _playbooks_ directory. Because the project makes use of ansible role structure, the playbook contains only definitions of the roles, and all the logic is perfomed by them, thus making the project both granular and easy to maintain.

The playbook uses the following roles:

* **activemq** - deploys and configures Apache ActiveMQ
* **adw** - deploys and configures Alfresco Digital Workspace
* **common** - contains a set of common tasks that prepares the specified host for other roles (creates user and group, common directories)
* **java** - deploys OpenJDK
* **nginx** - deploys and configures Nginx as a proxy
* **postgres** - deploys and configures PostgreSQL
* **repository** - deploys and configures Alfresco Repository and Alfresco Share
* **search** - deploys and configures Alfresco Search Services
* **sfs** - deploys and configures Alfresco Shared File Store
* **sync** - deploys and configures Alfresco Sync Service
* **tomcat** - deploys and configures Apache Tomcat
* **transformers** - deploys and configures Alfresco Transform Service
* **trouter** - deploys and configures the Transform Router

The same playbook can be run to deploy the system in several different ways, please refer to the [deployment guide](./deployment-guide.md) for a step by step set of instructions.

## Versioning

The playbooks have been tested with Ansible 2.9.18 on target hosts with the following operating systems:

* CentOS 7 and 8
* Red Hat Enterprise Linux 7 and 8

The table below shows the version of the components deployed by the playbook for ACS 7.x and 6.2.N.

| Component | 7.0 Enterprise | 6.2.N Enterprise | Community |
|-|-|-|-|
| OpenJDK | 11.0.7 | 11.0.7 | 11.0.7 |
| Apache Tomcat | 9.0.41 | 8.5.56 | 9.0.41 |
| PostgreSQL | 13.x | 11.x | 13.x |
| Apache ActiveMQ | 5.16.1 | 5.15.13 | 5.16.1 |
| Repository | 7.0.0 | 6.2.2 | 7.0.0 |
| Share | 7.0.0 | 6.2.2 | 7.0.0 |
| Search Services | 2.0.1 | 1.4.3 | 2.0.1 |
| All-In-One Transformation Engine | 2.3.10 | 2.3.10 | 2.3.10 |
| AOS | 1.4.0 | 1.3.1 | 1.4.0 |
| GoogleDocs | 3.2.1 | 3.2.0 | 3.2.1 |
| Digital Workspace | 2.1.0 | 2.1.0 | N/A |
| Transform Router | 1.3.2 | 1.3.2 | N/A |
| Shared File Store | 0.13.0 | 0.13.0 | N/A |
| Sync Service | 3.4.0 | 3.3.3.1 | N/A |
