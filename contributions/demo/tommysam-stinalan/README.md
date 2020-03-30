# Demo Proposal
## Members
Tommy Samuelsson (tommysam@kth.se)
Stina Långström (stinalan@kth.se)

## Topic
Data corruption

The idéa is to securly use fetched data in applications. So the application in it self can relay on that data it will use in different components won't crash the application. If a data set is demed corrupted it will discard it then notfiy ennd user that data with ID:# was not renderd. (Notification can be via slack, mail or similar).


## Demo
Two live pages the receive the same data. But the one not using the "data corruption handler" will crash when they receive the corrupted data set. 
The demo could be interactive by having a input field(s) for data. Allowing the demo-viewer to try to crash the site's. (Hopefully only one will crash)