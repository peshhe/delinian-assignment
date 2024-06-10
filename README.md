# Python with Flask web-app | Delinian

This repository contains the Python source code and necessary files to build a Docker image, which is then pushed to Azure Container Registry and deployed to Azure Container Instances using GitHub Actions.

> **_NOTE:_** This README.md file is still under development.


## Table of contents

- [Assignment](#objective-definition)
- [Solution Overview](#solution-overview)
- [Prerequisites](#prerequisites)
- [Usage](#usage)


## Project's assignment
<details><summary>

#### Objective definition</h4></summary>
Fork a repository that contains a simple web application or generate one yourself inside GitHub. The stack is up to you and what you feel comfortable with as long as you have:
* An API or Web App
* Optional: Deploy a relational database to Azure and link it to the web app or API
* Optional: Perform simple read/write operations
* Containerise the application and create a docker image and upload it to Azure Container Registry.
* Strictly Optional: Include in-memory storage like Redis if your app has the functionality for it.

#### CI/CD Pipeline using GitHub Actions
Write a GitHub Actions workflow that performs the following steps:
* Checkout the code.
* Build the docker image.
* Upload docker image
* Deploy it to Azure Container instance or Azure Container app.
* Configure Environment Variables & Connection Strings

#### Deploy the environment using Terraform Azurerm provider and push the .tf files in GitHub repository.
The pipeline should only deploy to Azure when the changes are merged via approved Pull Request to the production branch of choice. 
 
In a situation where you cannot complete the whole task, you can still be given the chance to talk about the challenges and how you would have solved the problems / implemented solutions even though they are incomplete. **Expected time for completion(Monday)**
 
Write a README.md file documenting how the CI/CD pipeline works, and any prerequisites for running it, including the docker image
Submit the repository being public or if private be willing to provide access.
</details>


## Solution overview
The inspiration for this web app and the source code has been taken from <a href="https://github.com/jakerieger/FlaskIntroduction">this GitHub repo</a>. It is simulating a "To Do" tasks manager, where you can add, update and remove tasks.

This solution uses the Python <a href="https://flask.palletsprojects.com/en/3.0.x/">Flask</a> Web Framework.

As per the assignment's requirements this web-app performs basic CRUD (Create, Read, Update, Delete) operations to a Database. The connection to the Database as well as the manipulations are achieved with the help of <a href="https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/">Flask-SQLAlchemy</a> - a Flask extension.

The source code has been modified <!--to read environment variables-->for establishing a connection to a PostgreSQL Database Server. The DB server has to be deployed in Azure, using the <a href="https://github.com/peshhe/assignment-terraform">Terraform repo</a> 

## Prerequisites

Before running the automation in this repository, ensure that the necessary infrastructure is set up using the [assignment-terraform](https://github.com/peshhe/assignment-terraform) repository.

In order for the automated GitHub Actions Workflow (CI/CD pipeline) to run successfully you will also need to set up the Azure credentials as GitHub Actions Secrets in the GitHub repo.

In the GitHub UI, navigate to your forked repository and select Security > Secrets and variables > Actions. Select New repository secret to add the following secrets one by one:

|Secret|Value|
|---|---|
|`AZURE_CREDENTIALS`| The entire JSON output from the service principal creation step
|`REGISTRY_LOGIN_SERVER`| The login server name of your registry (all lowercase). Example: myregistry.azurecr.io
|`REGISTRY_USERNAME`| The `clientId` from the JSON output from the service principal creation
|`REGISTRY_PASSWORD`| The `clientSecret` from the JSON output from the service principal creation
|`RESOURCE_GROUP`| The name of the resource group you used to scope the service principal

## Usage
To be updated
> **_NOTE:_** There is an update for the Python app coming in. It will use environment variables with default values, instead of hardcoded ones, in case the environment value is missing.

Stay tuned.