# 🔑 Key Azure Services Overview with Details and Pricing

## ⚡ Azure Functions

Azure Functions is a **serverless compute service** that lets you run event-driven code without provisioning or managing servers.

- **How it works**:  
  - Write small functions triggered by events such as HTTP requests, timers, or messages from queues.  
  - Azure automatically allocates compute resources and scales based on demand.  
  - You only pay for the time your code runs and the number of executions.

- **Pricing**:  
  - First 1 million requests per month are free.  
  - $0.20 per million executions thereafter.  
  - Additional cost based on memory size and execution time (GB-seconds).

---

## 🗄️ Azure SQL Database

Azure SQL Database is a **fully managed relational database** built on SQL Server technology.

- **How it works**:  
  - You create a database instance hosted on Azure infrastructure.  
  - Azure handles backups, patching, high availability, and scaling automatically.  
  - Supports familiar SQL language and tools for development and management.  
  - Offers options for performance tiers (DTU or vCore models) based on workload needs.

- **Pricing**:  
  - Basic tier starts around $5/month (DTU-based).  
  - vCore-based pricing begins at about $15/month, with flexibility to choose compute and storage independently.  
  - Backup storage and data egress are charged separately.

---

## 📊 Power BI Service

Power BI is a **cloud-based business analytics service** to visualize and share insights from your data.

- **How it works**:  
  - Connect to a variety of data sources including Azure SQL Database.  
  - Create interactive reports and dashboards using a drag-and-drop interface.  
  - Data refresh can be scheduled or real-time with DirectQuery.  
  - Share dashboards with others within your organization or embed them in web applications.

- **Pricing**:  
  - Power BI Free: Personal use, no sharing capabilities.  
  - Power BI Pro: $9.99/user/month, allows collaboration and sharing.  
  - Power BI Premium: Starts around $20/user/month or dedicated capacity pricing for enterprise features.

---

## 🛡️ Azure Key Vault

Azure Key Vault is a **secure cloud service** for managing cryptographic keys, secrets, and certificates.

- **How it works**:  
  - Store secrets like database connection strings, API keys, and certificates securely.  
  - Access to secrets is controlled via Azure Active Directory identities and policies.  
  - Azure services such as Functions can retrieve secrets dynamically at runtime without hardcoding sensitive information.

- **Pricing**:  
  - $0.03 per 10,000 operations (including reads and writes).  
  - Additional charges apply if using dedicated hardware security modules (HSMs).

---

## 🔌 Azure Logic Apps

Azure Logic Apps is a **low-code/no-code workflow automation service**.

- **How it works**:  
  - Create workflows by connecting triggers and actions visually.  
  - Integrate with hundreds of connectors (HTTP, SQL, Blob storage, SaaS services).  
  - Schedule or event-trigger workflows that automate data movement, transformation, and business processes.  
  - Useful for orchestrating multi-step integrations without writing extensive code.

- **Pricing**:  
  - Consumption-based: roughly $0.000025 per action executed.  
  - Premium plans available for isolated environments and enhanced SLAs.

---

## 🖥️ Azure App Service

Azure App Service is a **fully managed platform for hosting web apps and APIs**.

- **How it works**:  
  - Deploy web applications built with .NET, Node.js, Python, Java, and more.  
  - Supports continuous deployment from GitHub, Azure DevOps, or local Git repositories.  
  - Built-in auto-scaling, custom domains, SSL certificates, and authentication features.  
  - Manage staging slots for zero-downtime deployments.

- **Pricing**:  
  - Free and shared tiers provide basic hosting for testing or development.  
  - Basic tier starts at approximately $13/month.  
  - Standard and Premium tiers offer more CPU, memory, and advanced features, with prices scaling accordingly.

---

## 📦 Azure Container Instances & Azure Kubernetes Service (AKS)

For advanced deployment and container orchestration:

- **How it works**:  
  - Azure Container Instances (ACI) allows you to run containers without managing servers.  
  - Azure Kubernetes Service (AKS) is a managed Kubernetes environment for large scale container orchestration.

- **Pricing**:  
  - ACI is billed per second for CPU and memory resources consumed.  
  - AKS control plane is free, but you pay for the underlying VM nodes.

---

## 🛠️ Azure DevOps / GitHub Actions

CI/CD pipelines and version control integration:

- **How it works**:  
  - Automate build, test, and deployment workflows.  
  - Integrate with Azure Functions, App Service, AKS, etc.  
  - Manage source code repositories and issue tracking.

- **Pricing**:  
  - Azure DevOps offers free tier with limited build minutes and users.  
  - Paid tiers increase build minutes and user licenses.  
  - GitHub Actions includes free minutes for public repositories; private repo minutes depend on plan.

---

## 🔍 Azure Monitor & Application Insights

For monitoring, logging, and alerting:

- **How it works**:  
  - Collect and analyze telemetry from apps and infrastructure.  
  - Set up alerts for failures, performance issues, or thresholds.  
  - Provides deep insights into app health and user behavior.

- **Pricing**:  
  - Free tier with limited data retention and volume.  
  - Paid pricing based on data ingested and retention duration.

---

💡 **Note:** Pricing and features vary by region and usage. Use the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) for detailed cost estimates.
