# 🚆 Azure Train Data Project with iRail API

- Repository: `challenge-azure`
- Type of Challenge: `Learning`
- Duration: `5 days`
- Deadline: `dd/mm/yy H:i AM/PM`
- Team challenge : `solo`

## Azure Setup
You'll be provided a @becode.education Microsoft account.

Use it to create an Azure account here:
https://portal.azure.com/#home

Once it's done start **Azure for Students**. Thanks to this you won't need to register a credit card and you'll get:

- $100 credit to spend in Azure
- Free services

More information here: https://azure.microsoft.com/en-us/free/students/

When the setup is done you can start creating resources!

![alt text](assets/azure-for-student.png)

## 🎯 Project Overview

Create a real-world data pipeline that fetches train departure data from the [iRail API](https://docs.irail.be/), normalizes it, and stores it in a SQL database — all deployed using Microsoft Azure.

This project is structured in three progressive levels:

- 🟢 **Must-Have**: Set up core functionality — fetch and store data via Azure Portal using Azure Functions and Azure SQL Database.
- 🟡 **Nice-to-Have**: Add automation (scheduling), build a live dashboard (e.g., Power BI), and enable data refresh.
- 🔴 **Hardcode Level**: Explore full DevOps integration — CI/CD pipelines, scripting with Azure CLI, Docker deployment, and cloud-native infrastructure as code.

👉 **Important:** You must complete the *Must-Have* stage first. However, it's crucial that you **think ahead to what kind of dashboard or insights you might want to build** (in Nice-to-Have and Hardcore Level). This will help you design the right data schema and fetch meaningful data now — avoiding the need to start over later.

## 🧠 Project Vision

Using the [iRail API](https://docs.irail.be), your mission is to create a **live, cloud-native dashboard** that gives insight into train operations in Belgium. You'll gather real-time public transport data, structure and store it in the cloud, and visualize it in a way that's useful and meaningful.

You're encouraged to bring **your own ideas and creativity**. The iRail API offers a variety of data: live departures, delays, connections, train routes, and more. Your final dashboard should **tell a story**, answer real-world questions, or help someone make smarter decisions about train travel.

## 💡 Example Use Cases to Consider Early

These are some potential directions your dashboard could take. Pick one early to help you decide:

- **Live Departure Board**: Show current or recent train departures for a selected station
- **Delay Monitor**: Track which stations or trains experience the most delays over time
- **Route Explorer**: Let users check travel time and transfer info between two cities
- **Train Type Distribution**: Visualize where and how different train types (IC, S, etc.) operate
- **Peak Hour Analysis**: Show how train traffic and delays vary by time of day or week
- **Real-Time Train Map** (advanced): Plot moving trains with geolocation

🧭 **Plan ahead**: Even though you’re currently focusing on fetching and storing data, choose a use case now so you start downloading the **right endpoints and fields** (e.g., platform, delay, train type, connection route). This makes later stages easier and more meaningful.

## 🟢 Must-Have: Azure Function Pipeline via Azure Portal

### Objective  
Use the Azure **web portal** (no CLI) to deploy a **Python Azure Function** that fetches live train data and inserts it into an **Azure SQL Database**.

### Azure Services Used

| Azure Service              | Purpose                                       |
|---------------------------|-----------------------------------------------|
| Azure Function App (Python) | Run data ingestion logic as a serverless app |
| Azure SQL Database         | Store normalized train data                   |
| Azure Storage Account      | Dependency for Function App                  |
| App Service Plan (Consumption) | Host the Function with autoscaling      |

### Steps

1. **Create Azure SQL Database** via the portal:
   - Use the “Create a resource” wizard
   - Set up firewall to allow external IP
   - Note the connection string for later use

2. **Create an Azure Function App**:
   - Use “Python 3.10” as the runtime
   - Deploy an HTTP-triggered function using the web editor
   - Use environment variables for credentials (in App Settings)

3. **Implement the logic** to:
   - Call the iRail API (`/liveboard` or /`connections`)
   - Normalize the JSON using Python libraries (e.g., pandas)
   - Connect and write to Azure SQL

4. **Test the Function** directly from the portal and verify that the data appears in your SQL table.

### Deliverables

- ✅ Deployed Azure Function (HTTP endpoint)
- ✅ Azure SQL DB with at least one filled table
- ✅ Documentation (README) describing your process
  
## 🟡 Nice-to-Have: Automation, Power BI, and Scheduling

### Objective  
Extend the project by automating data ingestion and building live dashboards.

### Additions

1. **Scheduled Data Fetching**
   - Add a **Timer Trigger** to your Function App
   - Fetch new data every hour (or another interval)
   - Ensure duplicate entries are handled in your SQL table

2. **Live Power BI Dashboard**
   - Connect **Power BI Service (online)** to Azure SQL
   - Create visuals: bar charts, line graphs (e.g., trains per hour)
   - Publish and embed the dashboard (optional)

3. **Improved Data Schema**
   - Normalize additional fields like platform, status, vehicle type
   - Use proper SQL data types: `DATETIME`, `INT`, `VARCHAR`

4. **Logging & Monitoring**
   - Use Azure Application Insights for runtime metrics and error tracking
   - Log custom events in your Function

## 🔴 Hardcore Level: CI/CD, Azure CLI, and DevOps Automation

### Objective  
Take your project to production-grade deployment using DevOps practices and cloud scripting.

### Advanced Features

1. **CI/CD Pipeline**  
   - Automate building, testing, and deploying your Function App and infrastructure.  
   - Use GitHub Actions or Azure DevOps Pipelines for repeatable, reliable delivery.

2. **Infrastructure as Code with Terraform**  
   - Define and provision Azure resources declaratively using Terraform configs.  
   - Enables version-controlled, repeatable infrastructure deployments integrated into your pipeline.

3. **Azure CLI and Scripting Automation**  
   - Write Python or shell scripts to automate Azure resource management and configuration tasks.  
   - Useful for custom setup steps not covered by Terraform or CI/CD tools.

4. **Authentication and Security Best Practices**  
   - Implement Managed Identities to avoid hardcoded secrets.  
   - Secure Function endpoints with OAuth, API keys, or Azure AD integration.

5. **Containerization with Docker**  
   - Package your Azure Function or pipeline code in Docker containers.  
   - Deploy containers to Azure Container Registry and run via Azure Functions Premium Plan or Azure Container Apps.


## 📝 Evaluation Criteria

| Category                      | Must-Have | Nice-to-Have | Hardcore Level     |
|------------------------------|--------------|----------------------|----------------------------|
| Function App is deployed     | ✅            | ✅                    | ✅                          |
| SQL DB contains live data    | ✅            | ✅                    | ✅                          |
| Code structure and clarity   | Basic        | Good abstraction     | Modular, reusable          |
| Automation & scheduling      | ❌            | ✅                    | ✅ with pipeline automation |
| Dashboard                    | ❌            | ✅ Power BI Live      | ✅ Auto-refresh + embed     |
| Deployment strategy          | Manual       | Partial scripts      | Full CI/CD pipeline         |
| Use of environment configs   | Basic         | Partial              | Secrets vault or managed ID|


## ✅ Submission Checklist

- [ ] GitHub repo with all source code and README
- [ ] Screenshot of Function App test run
- [ ] Screenshot of SQL data table
- [ ] If applicable, link to Power BI dashboard
- [ ] (Optional) CI/CD pipeline config and diagram


## 🔚 Final Notes

- Focus first on getting your **Function App to insert real data**
- Treat each level as an **independent milestone**
