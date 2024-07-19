## Required Steps (New YouTube Channel)

- Own Your Domain
- Setup Google Workspace with Your Domain
- Google Cloud Platform
    - Create Account Using a User (with Administrative Permissions) Belonging to Your Google Workspace
    - Create Project (and Select It)
    - Enable YouTube Data API
    - Grant `Organization Policy Administrator` to Self
    - Modify Service Account Key Creation Policy
    - Create Service Account
    - Generate Key for Service Account
- Google Workspace Admin
    - Grant Access to the Service Account
      - `https://www.googleapis.com/auth/youtube.readonly`
      - `https://www.googleapis.com/auth/youtube.upload`
- YouTube
  - Create an Account (Channel) using the Google Workspace Account

### Install Python Libraries

```shell
pip install python-dotenv google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client 
```
## Existing YouTube Channel

- Create a New Channel with Your Existing YouTube Channel
- Move Existing Channel to Brand Account (The New YouTube Channel You Created)
- Invite the Google Workspace Account as Owner
- Accept the Invitation Received by Google Workspace Account
- Make the Google Workspace Account the Primary Owner of the Channel Via Brand Account