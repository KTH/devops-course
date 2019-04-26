# Automatic Static Site Redeploys

## Group members

- Toni Karppi (tonik@kth.se)
- Kristian Alvarez Jörgensen (krijor@kth.se)

## Description

The JAMstack is a modern web development architecture based on prebuilding sites at compile time, handling interactions with databases though general APIs, and handling dynamic content with Javascript (https://jamstack.org/). This architecture is interesting since it allows us to host plain old HTML files, which makes sites really fast. This is similar to how websites used to be served at the beginning of the web. The problem with serving regular HTML files was the difficulty of handling user content. The solution that the JAMStack proposes is to fetch the data from a CMS (or any data source) during compile time. If the content changes, the CMS notifies the website host using webhooks, and the entire site is rebuilt with the updated content. 

For this demo we will be using the GatsbyJS static site generator (https://www.gatsbyjs.org/). For the CMS we will be using Netlify CMS (https://www.netlifycms.org/). The demo will consist of a user adding some content to the CMS, and witnessing the host (Netlify) get a signal to rebuild the site. After the site has been rebuilt and redeployed, the user should see their content on the website.

