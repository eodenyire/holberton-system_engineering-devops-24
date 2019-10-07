# 0x19. Postmortem

Postmortem, is the roadmap for when an incident occurs in a process or several, where the company or its stakeholders are affected, finding the fault is a priority, the clock is in countdown, the support team must find the fault before the loss of resources and customers is unsustainable.

In many cases the processes of patching, updating or the lack of automation of processes, causes that there are reprocesses and cost overruns in operations, human failures also count.

## Context
For the entity in this case a bank, it is important to anticipate incidents, so it decides to make updates where the percentage of inquiries is less than 5%, the system is programmed so that 23 hours of each day processes of integration of the information.

## Issue
A customer of a premium account, who intends to pay for hotel services abroad for his family, by passing his silver card, finds that his card has been rejected, the terrified one, initiates the pertinent inquiries from his laptop.

## Timeline
Bank: Washington, 23:30 horas, Task: start information integration
Bank: Washington, 23:30 horas, Task: start backups in DBs,
Client: Isa Gates, Vietnam, 10:35 horas, Task: Balance inquiry: Overdrawn
Client: Isa Gates, Vietnam, hora 10:37 am, Task: check other balances: no movements
Client: Isa Gates, Vietnam, hora 10:39 am, Task: start chat with the bank
Bank: Washington, 23:40 horas, Task: Start customer support
Client: Isa Gates, Vietnam, hora 10:41 am, Task: dialogue about the problem
Bank: Washington, 23:44 horas, Task: Consult the platform: It does not allow access to customer information.
Client: Isa Gates, Vietnam, hora 10:45 am, Task: she cries and faints.
Bank: Washington, 23:46 horas, Task: Loses contact with the client.
Bank: Washington, 23:49 horas, Task: Issue an alert and scale the problem.
Bank: Washington, 23:59 horas, Task: Synchronization ends.
Client: Isa Gates, Vietnam, hora 11:35 am, Task: check balance: correct balance.
Bank: Washington, 7:00 horas, Task: Issues a statement to inform the automation and system integration operations, generates a gift of miles to the affected one, alternatives to the CTO are required to mitigate the impact of these processes.
Client: Isa Gates, Vietnam, hora 20:00 pm, Task: Receive an email from the bank where you apologize and authorize charging miles in favor.

## Conclusions
The CTO determines that the deployment of backups generates a block in the tables, mirror servers also upload where they do not have the relevant synchronization before starting the backpus, so the information is restricted for at least 1 hour, while other processes run that update the financial information of customers.

The CTO opens a tender to mitigate this failure.

The financial president determines that the operations carried out in these hours, impact clients abroad, being these large firms, or clients, are looking for alternatives with technology to mitigate this, it is decided to segment the regions and their clients, generate an investment in infrastructure in Europe and Asia, which allow the satisfaction of its customers in the medium term.

### this was what failed
When you start backup all tables of all databases are block, and only need is lock databases master

### Authors
Fesus Rocuts <https://github.com/fesusrocuts>

### See complete blog post
https://medium.com/@fesusrocuts/postmortem-2f82258859a1

