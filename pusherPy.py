import pusher

pusher_client = pusher.Pusher(
  app_id='1556681',
  key='276c6bb8aeb296ca6dba',
  secret='b07905fc2f39b34a20ab',
  cluster='ap2',
  ssl=True
)

pusher_client.trigger('sexy-channel69',
          'sexy-event',
          {"message": "Fuck me!",
           "priority": 1,
           "sender": "Arpit"
           })