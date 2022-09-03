from h_notify import *
import time
import traceback

default_token = '6879-5FJ3618KKG9E4VhXKOzQGw-GkyCJXxkSaG48xsPE7wY' # hypothesis api token for a user who is a member of all monitored groups
default_hook = 'https://hooks.slack.com/services/T03...yzy' # see https://YOUR_VANITY_NAME.slack.com/apps/manage/custom-integrations)

default_smtp_server = 'smtp.example.com' 
default_email_sender = 'hypothesis.notifier@example.com'
default_email_password = 'q1...Nm'

# while True:
try:
    # slack recipes

    # notify when an url in a list of urls of interest to the team is annotated
    # uses the wildcard_api endpoint
    notify_slack_url_activity(url='https://web.hypothes.is/*', token=default_token, pickle='urls', channel='test', hook=default_hook)

    # notify when there's an annotation from one among a list of users
    users = ['remiholden', 'jeremydean']
    for user in users:
        notify_slack_user_activity(user=user, token=default_token, pickle='users', channel='test', hook=default_hook) 

    # notify when there's an annotation in a group
    notify_slack_group_activity(group='8gk9i7VV', groupname='Anyone Can Join', token=default_token, pickle='AnyoneCanJoin', channel='test', hook=default_hook)

    # notify when there's an annotation with a specified tag
    notify_slack_tag_activity(tag='nextprez', token=default_token, pickle='nextprez', channel='test', hook=default_hook)

    # rss recipes 

    notify_rss_group_activity(group='jdLyRnR4', groupname='Anyone Can Join', token=default_token, pickle='jdLyRnR4')

    # email recipes

    notify_email_tag_activity(tag='futuoer', token=default_token, pickle='futuoer', smtp=default_smtp_server, sender=default_email_sender, sender_password=default_email_password, recipient='nobody@example.com')

    # print ( 'sleeping' )
    # time.sleep(60 * 30)  # wait 30 min to be polite to the hypothesis api
except:
    print ( traceback.print_exc() )


