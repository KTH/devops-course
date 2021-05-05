# Feedback on [#1258](https://github.com/KTH/devops-course/pull/1258)

## Members
Ioana Cotutiu (cotutiu@kth.se)

GitHub: [IC-kth](https://github.com/IC-kth)

## Feedback
Bellow is the feedback on Migrating a monolithic application to microservices, PR [#1258](https://github.com/KTH/devops-course/pull/1258).

## Feedback content

- [Overall opinion](#overall-opinion)
    - [Main strengths](#main-strengths)
    - [Main potential improvements](#main-potential-improvements)
- [Detailed feedback step by step](#detailed-feedback-step-by-step)
- [Grammar](#grammar)   
- [Conclusion](#conclusion)


## Overall opinion

First of all, congratulations on the work you have put into this tutorial! The topic you chose is of great interest not only to DevOps but in general to the industry since microservices are slowly becoming the norm in software development. 

Overall, the tutorial is well-structured and has a logical flow that guides the user through the process of converting/migrating a monolithic application to a microservices-based one. The content is suitable for an intermediate user with limited knowledge about microservices and can be comfortably understood and executed within a time frame of about 15-25 minutes, even less when the user has some previous knowledge about the topic.

In general, executing the provided commands went well, except in later steps, an aspect that I am going to address in detail in [step 4](#step-4) and [step 5](#step-5).

Bellow, I highlight the main strengths and potential improvements that I identified for this tutorial. For detailed feedback on each step see the [Detailed feedback step by step](#detailed-feedback-step-by-step) section.

   #### Main strengths
   
   - The tutorial uses some Katacoda features that make it easy for the user to execute commands and navigate between files. These include:
        - the editor for viewing and editing the project files, which is an easier alternative to linux text editors like vi and vim;
        - tabs which act as quick links for viewing the results of the requests sent to each microservice;
        - the use of the execution feature provided by Katacoda is a great alternative for writing commands in the terminal (especially long ones).
   - The possibility of choosing whether to use the predefined files or code along by adding code to the provided template files ensures a learning experience adapted to different learner types.
   - The Tips and Observation sections inserted throughout the tutorial are a good way of pointing out important aspects.
   - The existence of a GitHub repository with the project discussed in the tutorial gives the possibility to further explore the topic, starting from a simple project/example.
   - By providing a pros and cons of the microservice architecture section as well as a take away section, the user can achieve a better understanding of the topic beyond just commands and code.  
   
   #### Main potential improvements
   
   - For further learning and clarifications regarding different concepts and tools presented/used in the tutorial, links to external sources might come as useful (see the Links section for each step, when applicable).
   - Some hardcoded links point to changing URIs ([see step 4](#step-4)). These make it impossible to access the underlying services.
   - Some code samples ([see step 4](#step-4)) that need to be added in files are syntactically incorrect as of Java syntax rules, and generate build errors.
   - There are multiple spelling and grammar mistakes throughout the tutorial which should be fixed ([see Grammar](#grammar)).
   - To make it even easier to copy and paste code from the provided snippet to the associated file in the code editor you can use the [clipboard integration](https://katacoda.com/scenario-examples/scenarios/clipboard) provided by Katacoda. This will copy the code to the user's Clipboard and then the code can be pasted into the file as usual (eg. CTRL + V). This is useful when you have longer code snippets, so you can avoid having to select everything using the mouse. 
   - Since you are using the **execute** feature provided by Katacoda, which runs the provided command in the terminal, it is worth mentioning the problem that comes with using it. You are running services, that must be stopped using the *CTRL + C* command, before running the next command. However, when using the **execute** command you can have the case when the service is still running, and the user pressed execute for another command. This results in the command being displayed in the terminal with no action, or in some cases it produces some errors. To avoid this I would suggest using the [interrupt](https://www.katacoda.community/scenario-syntax.html#interrupt) command provided by Katacoda, together with the **execute** command. This will perform a **CTRL + C** operation to stop any running command, before executing the current one.
   
## Detailed feedback step by step

In this section of the feedback I address in detail potential improvements that can be made in each step of the tutorial.
In general each step will contain the following parts:

   - Strength - what is good about this step
   - Improvement - improvements that can be made to code snippets or text parts
   - Links - links to additional material that can be useful for applying the suggested improvement (when applicable)
   
   **Note:** 
   
   *Since the source code with the corresponding steps for the Katacoda tutorial is not provided I cannot directly link each improvement suggestion to the corresponding .md file. However, I will try to make it as clear as possible what and where is the potential improvement.* 
   
  #### Introduction
   
   - Strength
       - The learning outcomes and the structure of the tutorial are clearly outlined from the very start, which is good for getting an idea of what and how you will learn. 
   - Improvement
       - Only for consistency reasons, I would suggest using either **monolith** or **monolithic** throughout the tutorial, but not both.
   
  #### Step 1
   
   - Strength
       - Information regarding the Katacoda environment and the project structure is clearly stated. This is helpful for getting used to the Katacoda environment and the project.
       - I think that for the learning process is very good that you include a try-it-yourself exercise at the end of this step.
   - Improvement
       - You indicate that the Monolith tab should only be opened after the "Completed initialization" has been displayed in the terminal. However, this is never displayed or displayed after opening the Monolith tab(behaviour reproduced in 2 browsers namely Google Chrome and Firefox). Therefore, to avoid this misleading situation I suggest that you point to the moment when *Started MonolithicApplication in X seconds (JVM running for Y)* occurs, since it marks the moment when your application is up and running and can receive requests.
       - Even if you capture the essence of what a monolithic application is, I would suggest adding some links for more in-depth information on the topic. Also, it is often considered a good practice to link the documentation of the hosting platform (in your case Katacoda). This might be useful as additional help on how to interact with the platform.
   - Links
       - Link to [Katacoda documentation](https://www.katacoda.community/welcome.html);
       - Links to further information about monolithic applications (such as [Wikipedia](https://en.wikipedia.org/wiki/Monolithic_application), or [other sources](https://microservices.io/patterns/monolithic.html))
  
  #### Step 2
  
   - Strength
       - A clear flow of the steps that need to be executed as well as shortcuts to the files that need to be changed are provided. It is very useful that you provide the editor to ease the navigation and file changing process, which would be more difficult when performed in the terminal.
   - Improvement
       - The mapping you made in the code for retrieving a Podcast object with a given id is **podcasts/{podcastId}**. However, before the code snippet, the explanatory text that precedes it refers to the mapping as **podcast/{podcastId}**. This is not a major issue in itself, but can be confusing seeing two different mappings.
       - Even if the short description of what a microservice-based application is might be enough for the purpose of this tutorial, I would suggest adding some links for more in-depth information on the topic. I think this is also important to better understand the *pros and cons of microservices* section of the tutorial (step 5).
   - Links
       - Links to further information about microservices (such as [Wikipedia](https://en.wikipedia.org/wiki/Microservices), [Spring's view on the topic](https://spring.io/microservices) (especially since you are using SpringBoot) or [microservices.io](https://microservices.io/))
  
  #### Step 3
  
   - Strength
       - I think it is very good that you provide the *Rating* and *UserRating* classes, so that the focus stays on the microservice and the logic behind it.
   - Improvement
       - For easing the access to the specified classes in the *models* package, I would suggest using the **open** command, as you did for accessing other files.  
       - Since you provide a template file that needs to be filled with the specified code I think it is better to either provide just the code that needs to be added or have the template include just the imports to avoid confusion. For example, in the RatingDataResources template you include the class declaration, without the preceding annotations. Therefore, when performing copy-paste you might copy just the code inside the class, and miss adding the annotations, which will create issues.
        
       ```java
         public class RatingDataResources{}
       ```        
       vs.
        
       ```java
         @RestController
         @RequestMapping("/ratingdata")
         public class RatingDataResources{}
       ```                     
         
  #### Step 4
  
   - Strength
       - It is good that you explain the reason why the URIs used in the code are strangely-formatted and that you provide their equivalent in local execution.
       - It is very useful that you mention the need for the other two services to be up and running for this service to function properly.
   - Improvement
       - The URIs that you are using for retrieving data from the microservices seem to not be static. The one that you are using is different from the ones generated in each session/ account session. For example, I got all this URIs when running your tutorial from different browsers and accounts:
         - https://2886795346-8083-host08nc.environments.katacoda.com/ratingdata/users/Katacoda (the one you provided)
         - https://2886795364-8083-host08nc.environments.katacoda.com/ratingdata/users/Katacoda
         - https://2886795347-8083-host08nc.environments.katacoda.com/ratingdata/users/Katacoda
       - The code snippet that you provide for retrieving each podcast by id is syntactically incorrect as of Java syntax rules, and generates build errors. However, the code provided in the repository (in the finnish project) is correct, so I would recommend replacing the snippet with the correct code. You can see the difference bellow:      
       
       broken snippet
        
       ```java
          return.ratings.stream().map(rating->{
               Podcast podcast= restTemplate.getForObject("https://2886795346-8082-host08nc.environments.katacoda.com/podcasts/"+rating.getPodcastID, Podcast.class);
                return new Podcast(podcast.getName, "devOps",rating.getRating())
            }).collect(Collector.toList());
       ```        
       vs.
       
       code from repository 
       ```java
         return ratings.getUserRating().stream().map(rating -> {
                     Podcast podcast = restTemplate.getForObject("http://localhost:8082/podcasts/" + rating.getPodcastId(), Podcast.class);
                     return new CatalogItem(podcast.getName(), "Security", rating.getRating());
                 }).collect(Collectors.toList());
       ```     
      - In the code snippet that yo provide for retrieving the list of UserRatings you are using a non-existent mapping (see bellow). The actual mapping that is provided in the code is **/users/Katacoda**, and it doesn't include any variable-based mapping (/{userId} or other). The same issue can be found in the code from the repository, which in theory, makes this step of the tutorial non-executable online and locally. I would therefore, suggest fixing this issue both in the tutorial and the repository. In addition, since the variable mapping **/{userId}** becomes unused I would suggest removing that from the **getCatalog()** request mapping. 
      ```java
         UserRating ratings = restTemplate.getForObject("https://2886795346-8083-host08nc.environments.katacoda.com/ratingdata/users/"+userId, UserRating.class);
      ``` 
      - The mapping that you provide for retrieving the list of CatalogItem objects (from the podcast-catalog-service microservice) is different than the one you provide in the tutorial as a link in the podcast-catalog-service tab. I would suggest changing it so it matches the mapping provided in the code. You can see the difference bellow:
          ```
             /catalog/{userId}
             vs.
             https://2886795346-8081-host08nc.environments.katacoda.com/catalog/Katacoda
          ```
         
  #### Step 5
  
   - Strength
       - For a better understanding of the topic, beyond just lines of code, I think that this pros and cons of microservices section is very useful. 
   - Improvement
       - The second sentence of the *Effort while deploying* needs to be rewritten. I believe you meant that some code will be duplicated across microservices.
       - Since in this step you just briefly present some benefits and drawbacks of a microservice-based architecture, I suggest that you include some sources for more in-depth and detailed information.
   - Links
       - Links for microservices benefits and drawbacks ([microservices pros and cons](https://agilethought.com/blogs/microservices-pros-and-cons/), [5-pros-and-cons-of-microservices-explained](https://www.hitechnectar.com/blogs/5-pros-and-cons-of-microservices-explained/), [to-go-or-not-to-go-micro](https://medium.com/@goodrebels/to-go-or-not-to-go-micro-the-pros-and-cons-of-microservices-7967418ff06) or [cloudacademy blog](https://cloudacademy.com/blog/microservices-architecture-challenge-advantage-drawback/)) 
   
  #### Step 6
  
   - Strength
       - It is useful that this step begins with a short yet clear explanation of what a Discovery Server is and how this tutorial uses Eureka.
   - Improvement
       - The path you provide for editing the *DiscoveryServerApplication.java* file is incorrect. This should be replaced with the following path:
       
       ```monolithic-to-microservices/start-microservices/discovery-server/src/main/java/com/devops/discoveryserver/DiscoveryServerApplication.java``` 
       
       - I suggest rephrasing the following statement about adding the **@EnableEurekaServer** annotation:
       
       ```The only think we need to be is to add @EnableEurekaServer above the public class.```
       
       - Since there is a big chance people doing this tutorial might have limited or no knowledge about a Discovery Server and Eureka in particular, I think it would be useful to include some links to additional information.
   - Links
       - Link to [Eureka](https://github.com/spring-cloud/spring-cloud-netflix)
       - Link to information on [client-side-discovery](https://microservices.io/patterns/client-side-discovery.html), [service-registry](https://microservices.io/patterns/service-registry.html) and [spring-cloud-service-discovery-with-eureka](https://medium.com/swlh/spring-cloud-service-discovery-with-eureka-16f32068e5c7) 
   
  #### Step 7
  
   - Strength
       - Straightforward and clear instructions on how to register the Eureka clients and test everything.
   - Improvement
       - I think it is worth mentioning that the **service.application.name** defined in *.properties* file will replace the **IP:port** combination, to avoid using static URIs. 
       - The ratings-data-service URI ```http://ratings-data-service/ratingdata/users/``` needs to be changed since it contains an invalid mapping. In *RatingDataResources* class the associated mapping is: 
      
       ```java
          @RestController
          @RequestMapping("/ratingdata")
          public class RatingDataResources{
          
             @RequestMapping("/users/Katacoda")
             public UserRating getUserRating()
     ```
   
  #### Step 8
  
   - Strength
       - Ending the tutorial with a summary of the main concepts and ideas discussed is a great way to reinforce the intended learning outcomes.
   - Improvement
       - It might be useful, but not mandatory, to add links to similar tutorials or more advanced ones.
   - Links
       - Suggestion: [microservice-registration-and-discovery-with-spring-cloud-and-netflix-s-eureka](https://spring.io/blog/2015/01/20/microservice-registration-and-discovery-with-spring-cloud-and-netflix-s-eureka), 

## Grammar
   This section includes grammar and spelling mistakes that I found in the tutorial. To avoid adding a lot of extra text, this section will include just the misspelled word or grammatically incorrect group of words and the correct equivalent. I mainly added the most evident ones. These can be easily fixed using the find-and-replace mechanism found in most text editors.  However, I would recommend a grammar-checking tool (such as [Grammarly](https://www.grammarly.com)) to help you avoid grammar and spelling mistakes. 
   
   Generally speaking, **microservice** is spelled as a single word. However, throughout the tutorial you use **micro service**, **micro-service** and **microservice**. I would therefore, suggest changing all occurrences to **microservice**.
   
| Step number | Wrong | Right |
| :-: | :-: |:-: |
| **Step 1** | :x: | :heavy_check_mark: |
| | Kadacoda | Katacoda |
| | contain | contains |
| | name | a name |
| | availible | available |
| | webb brouser | web browser |
| | descripton | description |
| | Lets | Let's |
| **Step 2** | :x: | :heavy_check_mark: |
| | servise | service |
| | micro sevice | microservice |
| **Step 3** | :x: | :heavy_check_mark: |
| | fine | file |
| | same steps | the same steps |
| | for second | for the second |
| | It's consider | It's considered |
| | API | an API |
| | micro sevice | microservice |
| **Step 4** | :x: | :heavy_check_mark: |
| | must a servise | must be a service |
| | togehter | together |
| | call in | call it |
| | catalog-servise | catalog-service |
| **Step 5** | :x: | :heavy_check_mark: |
| | dublicated | duplicated |
| | componet | component |
| | micro serveses | microservices |
| | leads | lead |
| | independency | independence |
| | effect | affect |
| **Step 6** | :x: | :heavy_check_mark: |
| | theirs | their |
| | think | thing |
| **Step 7** | :x: | :heavy_check_mark: |
| | act as a | act as |
| **Step 8** | :x: | :heavy_check_mark: |
| | Independency | Independence |
| | effect | affect |   
        
## Conclusion

Going beyond the existing grammar and spelling issues, and some rather minor mapping mistakes, this tutorial is well-structured and captures the essential aspects of the associated topic, while following the established intended outcomes.

