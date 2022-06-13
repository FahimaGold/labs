# Terraform best practices

- Clean code: Although terraform is not a programming language, simlar rules of writing code apply to terraform as well.
- Knowing the infrastrcture: YOu need to know exactly what will be created and managed by terraform, particularly when using third-party modules as it becomes crucial to know and understand what resources will be created and what parameters to use.
- Seperating infrastrcuture from configuration: As it reduces complexity.
- Using one state per environment
- Configuring a backend
- Keeping backends small
- Not commiting the `.tfstate` file
# Screenshots of VMs

![vagrant status](./images/vagrant_status.png)
![screenshots from VirtualBox](./images/vms_from_virtualbox.png)
![AZ VM 1](./images/AZ_VM_1.png)
![AZ VM 2](./images/AZ_VM_2.png)
![AZ VM 3](./images/AZ_VM_3.png)
![AZ VM 4](./images/AZ_VM_4.png)
![AZ VM Poral](./images/AZ_VM_PORTAL.png)