# Auto-VPN: On-Demand WireGuard VPN Server Manager 
[![GitHub license](https://img.shields.io/github/license/g1ibby/auto-vpn)](https://github.com/g1ibby/auto-vpn/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/g1ibby/auto-vpn)](https://github.com/g1ibby/auto-vpn/stargazers)

Deploy your personal WireGuard VPN server with just a few clicks. No subscriptions, no complexity, full control.

![Main interface](images/main.png)

This project provides an effortless way to spin up your own temporary, cost-effective WireGuard VPN servers on-demand—no long-term subscriptions or complex manual setups required. By leveraging popular VPS providers like Vultr or Linode, it automatically:

- Deploys on Demand: Quickly launch a fresh VPS instance with WireGuard pre-installed.
- Easy Configuration: Generate and manage user profiles with a user-friendly GUI.
- Automatic Cleanup: Idle VPN servers are automatically torn down after a set period of inactivity, ensuring you only pay for what you use.
- Enhanced Privacy: Retain full control over your VPN infrastructure and connections, eliminating the need to trust external VPN services.

In short, this tool lets you enjoy a secure, private VPN connection whenever you need it and stop paying the moment you’re done.

## 🏃‍♂️ Quick Start

### Local Deployment (Docker)

1. Create a data directory:
```bash
mkdir data_layer
```

2. Run the container:
```bash
docker run --rm -d --pull always --name auto-vpn \
  -e USERNAME=admin \
  -e PASSWORD=qwerty \
  -e VULTR_API_KEY=<your-vultr-api-key> \
  -v $(pwd)/data_layer:/app/data_layer \
  -p 8501:8501 \
  ghcr.io/g1ibby/auto-vpn:main
```

3. Access the interface at `http://localhost:8501`

### Free Cloud Deployment (Render.com)

1. **Create New Web Service**
   - Sign in to [Render Dashboard](https://dashboard.render.com)
   - Choose "New Web Service"
   - Select Docker runtime
   - Use image: `ghcr.io/g1ibby/auto-vpn:main`

2. **Configure Environment Variables**
   
   Required:
   - `USERNAME`: Admin username
   - `PASSWORD`: Admin password
   - `VULTR_API_KEY` or `LINODE_API_KEY`: VPS provider API key
   - `SELF_URL`: Your Render service URL (e.g., https://your-service.onrender.com)

   Optional:
   - `DATABASE_URL`: PostgreSQL connection string (recommended for persistence)

3. **Deploy and Access**
   - Service will be available at your Render URL
   - Auto-ping feature keeps the service active on free tier

## 💻 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| USERNAME | Yes | Admin login username |
| PASSWORD | Yes | Admin login password |
| VULTR_API_KEY | * | Vultr API key |
| LINODE_API_KEY | * | Linode API key |
| SELF_URL | No | Service URL for auto-ping |
| DATABASE_URL | No | PostgreSQL connection string |

\* Either VULTR_API_KEY or LINODE_API_KEY is required

## 🏗️ Architecture

The project leverages several powerful technologies:

- **Pulumi**: Infrastructure as Code for VPS management
- **WireGuard**: Secure VPN protocol
- **Streamlit**: Modern web interface
- **Docker**: Containerization and easy deployment

## 🔒 Security Considerations

- All VPN traffic is encrypted using WireGuard
- No logs are kept on VPN servers
- Servers are automatically destroyed after inactivity
- Full control over infrastructure eliminates third-party trust

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- Pulumi: Handles infrastructure provisioning, making it simple to deploy and tear down VPS instances on-demand.
- [Nyr/wireguard-install](https://github.com/Nyr/wireguard-install): Automates the WireGuard installation process, ensuring a seamless setup experience.
- [Streamlit](https://streamlit.io): GUI
