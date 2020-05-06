This project is a part of the course DD2482-Automated Software Testing and DevOps, spring 2020.

## Demo: Data corruption

### Members

Tommy Samuelsson (tommysam@kth.se) & Stina Långström (stinalan@kth.se)

### Data corruption

*Data corruption is when data becomes unusable, unreadable or in some other way inaccessible to a user or application*
\- Technopedia

There are many factors that can trigger data corruption, which makes it hard to protect yourself. Malware infection is one common problem but a lot of problems are due to poor software and hardware, which includes both software bugs and hardware failure.

Data corruption can take several different shapes, for example file errors, including both permission changes and renaming, data incompatibility, configuration bugs and pipeline corruption (input and/or output) that cause user-facing issues. To protect against corrupted data one approach is to filter the data to prevent corrupted data from entering the system. It is also important to always have back-up on the data to be able to restore the data from a previously known good version. To protect against malware infection it is important to have good security, which includes antivirus systems but also checks of the existing data.

In this demonstration we aim to show how corrupted input data, from a file, a server or a user for example, can affect a running application. We want to show the difference of filtering the input vs not filtering the input and also show a back-log where information about corrupted data is displayed, to demonstrate the consequences of an unprotected environment.

### Demo

Link to the deployed demo: [demo](https://dd2482-demo-data-corruption.firebaseapp.com/)

Link to the screencast: [https://youtu.be/2voDWw1wz5Q](https://youtu.be/5ZgAnmygYAE)

Link to GitHub repository: [Data corruption](https://github.com/Zodbigt/dd2482_demo_data_corruption)

The demo consists of several options, that in general displays a new page. They are:

- **Background**

Information about this demo and data corruption in general.

- **Data generator**

A page which can generate input to the application. The user can choose between pre-made inputs or make an input themself. The self-made input is constructed as a field where the inputs should be typed and radiobuttons so that the user can choose with type the input should be in (String, Int, Null or Undefined) and accroding to these options the site will behave differently. 

- **Data safe mode**

The page which utilizes the data-safe-parser. Before data is displayed on this site the data goes though several checks to remove data that is currupted in some way. Only data that passes the system is showed on this site.

- **Regular mode**

This page shows the created data just like it is. No checks are made to the data before entering this site. Because of this, the data displayed on this site can look weird and the site can potentially crash as well if the data is very "bad".

- **Quarantined events**

All the data that got suspended from the Safe site end up here, with an explanation why is was suspended. This is an example of a log for corrupted data.

- **Clear the database**

This button clears the data of the database. This is nessesary if there exists some event that crashes the regular site, but can also be used to limit the information showed on the page.

## Grading citeria

The criterias we aim to fulfill with this demo are:

**The demonstration screencast is clearly motivated (why it matters for Devops?)** -We have an explanation under "Background" and we mention this in the beginning of the screencast as well.

**The demonstration screencast is difficult to do** -Yes, since the demo is interactive we needed to handle multiple users and connect the site to a database. All types of input needs to be handled as well.

**The demonstration screencasr is original** -Yes we hope so, we have at least never seen an interactive demo of data corruption.

**The demonstration screencast is sublime (eg visually appealing)** -The demo is made with styled components and are displayed as a website. Our goal is that users will find this demo easy to use and understand.

**The demonstration screencast contains an easter egg** -Yes.

**An accompanying Github repository has been made (optional)** -Yes.

**(From previous criterias) The audience can play / directly interact with the demo** Yes! And with a hosted app this can be done remotely as well (adaped to an online demo).
