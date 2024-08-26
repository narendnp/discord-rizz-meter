
# Rizz Meter

Rizz Meter is a fun Discord bot that lets you check your `!rizz` and once it gets to a certain number, it will grant you the ability to `!timeout` other user to further flex your rizz.

## Getting Started

You will need to both make a bot account on Discord and self-host the bot to have the bot running.

### Prerequisites

- Python >= 3.10

- pip >= 24.0

- Discord bot account with the required scopes (see below for setup)

- A role that is used to mute people

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/narendnp/discord-rizz-meter
   ```

2. Enter the directory
   ```sh
   cd discord-rizz-meter
   ```

3. Install the dependencies
   ```sh
   pip install -r requirements.txt
   ```

4. Create the config file
   ```sh
   mv config.json.example config.json
   ```

5. Manage your variables in `config.json` (details below)
   ```sh
   nano config.json
   ```

6. Run the bot
   ```sh
   python main.py
   ```

### Config
- `"GUILD_ID"`: Your server ID.

- `"TIMEOUT_ROLE_ID"`: The "muted" role (role you use to mute people)

- `"BOT_TOKEN"`: Your bot token.

- `"timezone"`: Your timezone/TZ identifier. Go [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to see your local TZ identifier. Defaults to Asia/Jakarta.

- `"rizz_threshold"`: The roll value required for the user to gain `!timeout` command. Defaults to 90.

### Creating Bot Account

1. Go to [Discord Developer Portal](https://discord.com/developers/applications) dashboard.

2. On the top right, click the blue **New Application** button.

3. Enter your desired bot name, then click **Create**.

4. On the left menu, click **Bot** (below OAuth2).

5. Click on the blue **Reset Token** button, then copy it. This is your `BOT_TOKEN` for the config file.

6. On the **Privileged Gateway Intents** section, toggle on all the three intents.

### Inviting the Bot

1. Open your bot's dashboard.

2. Click on **OAuth** on the left menu.

3. On the Scopes menu, check **Bot** permission.

4. On the Bot Permissions, check **Manage Roles**, **View Channels**, **Send Messages**, **Use Slash Command**.

5. Scroll down until you see **Generated URL**, copy the URL.

6. Paste it in a new tab, and invite your bot to your server.

### Server Setup

1. After you invite the bot, go to your server.

2. Turn on Developer Mode (Discord Settings - Advanced) if you haven't already.

3. Right click on your server icon, click **Copy Server ID**. This is your `GUILD_ID` for the config file.

4. Go to Server Settings - Roles.

5. Make sure the your bot's role is on top of the default role for your members and your "muted" role (the role you use to mute people).

6. Right click on that muted role, click **Copy Role ID**. This is your `TIMEOUT_ROLE_ID` for the config file.

## Usage

- `!rizz` to roll your rizz percentage.

- If your roll pass the rizz threshold, `!timeout @<user>` to timeout them for 30 seconds.

## To-do

- Multi-server support
- Create muted role upon invite
- ...

## Contributing

I'm a complete noob when it comes to building a Discord bot, so any contributions you make are **greatly appreciated**. After all, contributions are what make the open source community such an amazing place to learn, inspire, and create!

## Credits

- [othneildrew](https://github.com/othneildrew/Best-README-Template) for this readme template :)

