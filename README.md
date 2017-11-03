# discord-cron

A stupid bot that sends a message to said channel each X seconds.

Supports crontab syntax.

## Configuration
The only supported way to run this is through Docker, it'll work otherwise,
but you are on your own as to how to do this.

### Environment variables:
#### Authentication
  - `DISCORD_CRON_USER` - Email of the user
  - `DISCORD_CRON_PASS` - Password of the user

or:

  - `DISCORD_CRON_TOKEN` - Instead of user and password, use a token to login.
  
#### Schedule
- `DISCORD_CRON_CRONTAB` - Multiline parameter to schedule messages (interval, channel id, message)
  e.g.: 
  ```
  * * * * *, 31105814815614901265, :thinking:
  0 3 * * *, 31105814815614901265, hola!
  ```

