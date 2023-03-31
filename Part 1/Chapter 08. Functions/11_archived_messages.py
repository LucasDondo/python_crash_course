txt_msgs = ['Hello friend!', 'How are you?', 'Sounds good!', 'Bye friend!']
sent_txt_msgs = []


def send_messages(txt_msgs):
    ''' Prints txt. msgs. and moves them to sent_txt_msgs. '''
    while txt_msgs:
        current_txt_msg = txt_msgs.pop()
        print(current_txt_msg)
        sent_txt_msgs.append(current_txt_msg)


print('\n--- Text messages ---')
send_messages(txt_msgs[:])

print('\n--- Text messages in the original list ---')
for txt_msg in txt_msgs:
    print(txt_msg)

print('\n--- Sent text messages ---')
for sent_txt_msg in sent_txt_msgs:
    print(sent_txt_msg)
