version: "3.9"
services:
  worker:
    build: .
    environment:
      API_ID: $API_ID
      API_HASH: $API_HASH
      BOT_TOKEN: $BOT_TOKEN
      DOWNLOAD_DIR: $DOWNLOAD_DIR
      LOGGER: $logging
      OWNER_ID: $OWNER_ID
      PRO_USERS: $PRO_USERS
      MONGODB_URI: $MONGODB_URI
      LOG_CHANNEL: $LOG_CHANNEL
      BROADCAST_AS_COPY: $BROADCAST_AS_COPY
