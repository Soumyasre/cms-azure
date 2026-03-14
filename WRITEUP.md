### Analyze, choose, and justify the appropriate resource option for deploying the app.

**Virtual Machine:**
- Cost: Higher cost due to always-on infrastructure even when idle. Requires paying for the VM regardless of traffic.
- Scalability: Manual scaling required. Need to configure load balancers and scale sets separately.
- Availability: High availability is possible but requires manual configuration of redundancy.
- Workflow: Full control over OS and environment but requires more complex DevOps setup and maintenance.

**App Service:**
- Cost: Lower cost with Basic B1 tier. Pay only for the service plan, more economical for small apps.
- Scalability: Built-in auto-scaling with minimal configuration needed.
- Availability: Built-in high availability and load balancing managed by Azure.
- Workflow: Simple GitHub CI/CD integration, managed platform with no OS maintenance required.

**Choice: App Service**

I chose Azure App Service to deploy this CMS application because it provides a fully managed platform that eliminates infrastructure overhead. For a lightweight Flask web application, App Service is more cost-effective and easier to maintain than a VM. The built-in GitHub CI/CD integration made deployment straightforward, and automatic scaling ensures the app remains available without manual intervention.

### Assess app changes that would change your decision.

I would switch to a Virtual Machine if the application required custom OS-level configurations, specific software installations not supported by App Service, or needed to run background services and non-HTTP workloads. A VM would also be preferable if the application grew significantly in complexity and required greater control over networking and security configurations.
