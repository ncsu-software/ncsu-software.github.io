## Installation

### Installing Ruby & Jekyll

If this is your first time using Jekyll, please follow the [Jekyll docs](https://jekyllrb.com/docs/installation/) and make sure your local environment (including Ruby) is setup correctly.

### Installing Theme

Download or clone the theme.

To run the theme locally, navigate to the theme directory and run:

```
bundle install
```

To start the Jekyll local development server.

```
bundle exec jekyll serve
```

To build the theme.

```
bundle exec jekyll build
```

## Deployment

### Netlify

Use Netlify to deploy this theme. This theme contains a valid and tested `netlify.toml` - Feel free to use the 1-click deploy below.

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/zerostaticthemes/jekyll-serif-theme)

### Github Pages

This theme has been tested to work with Github Pages (and Github Project Pages). When using Github Pages you will need to update the `baseurl` in the `_config.yml` otherwise all the css, images and paths will be broken.

# Make

## Windows
- As Administrator Run
    ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

    ```bash
    choco install make
    ```
 
# Adding API Key (JSON) for google drive access:
    https://medium.com/@a.marenkov/how-to-get-credentials-for-google-sheets-456b7e88c430


# Authentication for GOOGLE API
  <ul class="current">
<li class="toctree-l1 current"><a class="current reference internal" href="https://docs.gspread.org/en/latest/oauth2.html#authentication">Authentication</a><ul>
<li class="toctree-l2"><a class="reference internal" href="https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project">Enable API Access for a Project</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account">For Bots: Using Service Account</a></li>
</ul>
</li>
</ul>
<ul>
</ul>

            


<u>
<h2><strong> Enable API Access for a Project</strong></h2>
</u>
Head to Google Developers Console and create a new project (or select the one you already have).

In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.

In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.


<u>
<h2><strong> For Bots: Using Service Account</strong></h2>
</u>

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs [sic].

Since it’s a separate account, by default it does not have access to any spreadsheet until you share it with this account. Just like any other Google account.

Here’s how to get one:


<u>
<h4><strong>Enable API Access for a Project if you haven’t done it yet</strong></h4>
</u>



Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.

Fill out the form

Click “Create” and “Done”.

Press “Manage service accounts” above Service Accounts.

Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.

Select JSON key type and press “Create”.

You will automatically download a JSON file with credentials. It may look like this:

```bash
{
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}
```

Remember the path to the downloaded credentials file. Also, in the next step you’ll need the value of client_email from this file.

Very important! Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google account. If you don’t do this, you’ll get a gspread.exceptions.SpreadsheetNotFound exception when trying to access this spreadsheet from your application or a script.

Move the downloaded file to ~/.config/gspread/service_account.json. Windows users should put this file to %APPDATA%\gspread\service_account.json.

Create a new Python file with this code:

```bash
import gspread

gc = gspread.service_account()

sh = gc.open("Example spreadsheet")

print(sh.sheet1.get('A1'))
```

Ta-da!


## Upload Research Papers

```bash
make upload-research-papers
```

## Download Google Sheets

```bash
make download-sheets-data
```

## Forms

- Researchers form: [Click here to access the form](https://forms.gle/72LCSdHEs63TW8HX7)
- News Form: [Click here to access the form](https://forms.gle/e4JEx8JXdhAzsvYh8)
- Labs Form: [Click here to access the form](https://forms.gle/wWqiUWXdP4KmX3pk8)
- Mantra Form: [Click here to access the form](https://forms.gle/L5Si1r8uYWhtBa4i8)
- Grants Form: [Click here to access the form](https://forms.gle/gyRANV7n4viQTVCP8)
- Employment Opportunity Form: [Click here to access the form](https://forms.gle/Mr2WEri7dKnR49947)
- Current Students Form: [Click here to access the form](https://forms.gle/BqtMafJgW1c6NYXV7)
- SuccessStories Form: [Click here to access the form](https://forms.gle/yT5Mu6NWesQTHmHZA)
## Research Papers

write TRUE to the select column in this research papers sheet that you want to display
- [Research Papers](https://docs.google.com/spreadsheets/d/1nQWPQR_ZeW5YDSQYa0uUTMx0rkRNMYk_BW1PR6OKyXI/edit#gid=739778209)