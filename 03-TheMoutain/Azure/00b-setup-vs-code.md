# Deploying Azure Functions Using Azure Extension in VS Code

## Prerequisites
- Visual Studio Code installed
- Azure Functions extension installed
- Azure Resources extension installed
- An active Azure subscription
- Azure Functions project created in VS Code

## Step-by-Step Deployment Guide

### 1. Sign in to Azure
- Open VS Code.
- Click on the **Azure** icon in the Activity Bar on the left.
- In the **Azure: Functions** area, click **Sign in to Azure**.
- Complete the sign-in process in the browser.

### 2. Prepare your Azure Function project
- Open your Azure Functions project folder in VS Code.
- Make sure your function app is working locally (optional: run with `func start`).

### 3. Create a Function App in Azure (if you don’t have one)
- In the **Azure: Functions** panel, click the **+** icon next to **Function Apps**.
- Follow the prompts:
  - Select your Azure subscription.
  - Provide a globally unique name for the Function App.
  - Choose a runtime stack (e.g., Node.js, Python, .NET).
  - Select the region.

### 4. Deploy your Function App
- Right-click the Function App you just created (or an existing one) in the **Function Apps** section.
- Click **Deploy to Function App**.
- Select your project folder when prompted.
- Confirm the deployment when asked to overwrite files (if applicable).

### 5. Monitor deployment
- VS Code’s Output panel will show deployment progress.
- Once completed, your Azure Functions app will be live.

## Additional Tips
- Use the **Azure Functions Core Tools** CLI (`func`) locally to test your functions before deployment.
- You can also configure deployment slots in Azure for staging and production environments.
- Set environment variables in Azure Portal under your Function App’s Configuration settings.

## References
- [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
- [Azure Functions Documentation](https://learn.microsoft.com/azure/azure-functions/)
- [Azure Function App Youtube tuto 3'](https://www.youtube.com/watch?v=7-P2hRFWmHY)
- [Azure Function in VS Code 4'](https://www.youtube.com/watch?v=p9JFMjU3LZ8)