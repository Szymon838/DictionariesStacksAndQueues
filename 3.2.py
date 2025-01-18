import queue

visited_websites = queue.LifoQueue()

visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
   website = input('Enter website name (0 for back): ')

   if website == '0':
      if visited_websites.empty():
         print('No websites in history.')
         break
      else:
         print('<-- Going back to a previously visited website')
         website = visited_websites.get()
   elif website != "":
      visited_websites.put(website) 

   print('You are currently viewing:', website)
   print()