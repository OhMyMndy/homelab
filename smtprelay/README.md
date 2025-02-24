# SmtpRelay

Send mail via msmtp:

```bash
source .env
echo "Test message from smtprelay" | msmtp --from "$REMOTE_USER" "$REMOTE_USER" --host=127.0.0.1 --tls=off --tls-starttls=off --port=25 --auth=off

```
