# Initial guest list
guests = ["Santi Baigorria", "Steve Jobs", "Lucas Gruden"]
hello = "! Would you like to come for dinner?"
print (f"{guests[0]}{hello}")
print (f"{guests[1]}{hello}")
print (f"{guests[2]}{hello}")
print ("I am inviting ", len(guests), "persons to dinner.")

# Bye Steve Jobs
print (f"{guests[1]} won't be able to come, since he is resting peacefully in hellos grave.")
guests[1] = "Elon Musk"
print (f"Inviting {guests[1]} instead.")
print (f"{guests[0]}{hello}")
print (f"{guests[1]}{hello}")
print (f"{guests[2]}{hello}")
print ("I am inviting ", len(guests), "persons to dinner.")

# Bigger table!
print ("I bought a bigger table! Now three more guests will come!")
guests.insert (0, "Manu Lostaló")
guests.insert (2, "Linus Torvalds")
guests.append ("Richard Hendricks")
print (f"{guests[0]}{hello}")
print (f"{guests[1]}{hello}")
print (f"{guests[2]}{hello}")
print (f"{guests[3]}{hello}")
print (f"{guests[4]}{hello}")
print (f"{guests[5]}{hello}")
print ("I am inviting ", len(guests), "persons to dinner.")

# Oh, no, problems!
print ("Problems ocurred, sadly. I am really sad, but only two of you will be welcomed at my house.")
no_longer_guest = guests.pop(0)
goodbye = "I am sorry, but you can no longer came, "
print (f"{goodbye}{no_longer_guest}.")
no_longer_guest = guests.pop(0)
print (f"{goodbye}{no_longer_guest}.")
no_longer_guest = guests.pop(1)
print (f"{goodbye}{no_longer_guest}.")
no_longer_guest = guests.pop(2)
print (f"{goodbye}{no_longer_guest}.")

# You are saved!
print (f"{guests[0]}{hello}")
print (f"{guests[1]}{hello}")
print ("I am inviting ", len(guests), "persons to dinner.")

# Empty list
del guests[0]
del guests[0]
print (guests)
