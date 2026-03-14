# Deployment Choice: App Service vs Virtual Machine

For this project, I chose Azure App Service instead of a Virtual Machine.

App Service provides a fully managed platform for hosting web applications without needing to manage infrastructure. It automatically handles scaling, patching, and deployment.

Advantages of App Service:
- Managed hosting environment
- Automatic scaling
- Built-in CI/CD deployment
- Integrated logging and monitoring
- Easy integration with Azure SQL and Blob Storage

Using a Virtual Machine would require manual configuration of the operating system, web server, and security updates.

Therefore, Azure App Service was the better option for deploying this Flask CMS application.
