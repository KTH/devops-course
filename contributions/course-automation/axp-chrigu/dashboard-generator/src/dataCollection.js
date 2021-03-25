const fs = require("fs");
const path = require("path");
const { title } = require("process");

// collectDashboardData().then(data => {
//     console.log(data);
// });

const repoUrl = "https://github.com/KTH/devops-course/tree/2021/";

// Traverse the project directory and look for all the contributions folders, collect task data on every folder
async function* traverse(dir) {

    for await (const d of await fs.promises.opendir(dir)) {
        const a = new Map();
        const entry = path.join(dir, d.name);
        if (d.isDirectory()) {
            if(d.name.includes('contributions')){
                const currentTime = new Date();
                // If folder name contains the year, use it, otherwise it is contributions for the current year
                year = isNaN(d.name.slice(-4)) ? currentTime.getFullYear() : parseInt(d.name.slice(-4))
                // Collect the data of a given years contributions
                yield* a.set(year, collectYearData(entry));
            }
            else{
                // Found non-task associated file, skip
                yield* traverse(entry);
            }
        }
    }
}

async function* collectYearData(dir){

    const categories = [];
    let taskCount = 0;
    // Go trough the directory and find all category directories
    for await (const categoryDir of await fs.promises.opendir(dir)) {
        if(categoryDir.isDirectory()){
            let categoryData = [];
            let entry = "";
            const categoryPath = path.join(dir, categoryDir.name);
            // Go trough all the task in a given category directory
            for await (const taskDir of await fs.promises.opendir(categoryPath)) {
                if(taskDir.isDirectory()){
                    // If folder is called weekX, its the presentation folder where tasks are divided into weeks,
                    // iterate over the specific week folders
                    if(taskDir.name.includes("week") || taskDir.name.includes("weak")){
                        entry = path.join(categoryPath, taskDir.name); 
                        for await (const presentationTaskDir of await fs.promises.opendir(entry)) {
                            if(presentationTaskDir.isDirectory()){
                                const presentationEntry = path.join(entry, presentationTaskDir.name+"/README.md");
                                
                                fs.readFile(presentationEntry, 'utf-8', (err, data) => {
                                    if(err){
                                        //console.error(err);
                                    }
                                    else{
                                        // Parse md file for authors, title and link
                                        const {title: t, authors: a} = parseMd(data);
                                        taskCount++;
                                        categoryData.push({'title': t, 'authors': a, 'link': repoUrl+entry});
                                    }
                                })
                            }
                        }
                    }
                    // Not the presentation folder, task folders are located here, read the task README and collect the data
                    else{
                        entry = path.join(categoryPath, taskDir.name+"/README.md");
                        fs.readFile(entry, 'utf-8', (err, data) => {
                            if(err){
                                //console.error(err);
                            }
                            else{
                                // Parse md file for authors, title and link
                                const {title: t, authors: a} = parseMd(data);
                                taskCount++;
                                categoryData.push({'title': t, 'authors': a, 'link': repoUrl+entry});
                            }
                        })
                    }
                }
            }
            categories.push({'name': categoryDir.name, 'tasks': categoryData});
        }
    }
    categories.unshift(taskCount);
    yield* categories;
}

// Parse a given string in md format, return authors, title and link of the task
function parseMd(mdContent){
    
    //Find title
    const titleRegex = /^# (.*$)/gim
    let title = titleRegex.exec(mdContent);
    if(title != null) {
        title = title[1];
    }

    // Find author
    const authorRegex = /(.*@kth.se.*)/gim
    let authors = mdContent.match(authorRegex);
    if(authors != null ) authors = authors.map(authString => {
        // Remove any unnessecary characters from beginning of author string
        let i = 0;
        while(i < authString.length) {
            if(authString[i] == " " | authString[i] == "*" | authString[i] == "-"){
                i++;
            }
            else{
                break;
            }
        }
        return authString.substring(i);
    });

    return {'title': title, 'authors': authors};
    
}

async function collectDashboardData() {
    const year = new Map();
    let totalTaskCount = 0;
    // Wait for all data items to be collected
    for await (const p of traverse('./')){
        const allItems = [];
        for await (const item of p[1]) {
            allItems.push(item);
        }
        // add number of tasks in year to the total number of tasks
        totalTaskCount += allItems[0];
        // Map the year of the contributions to its number of tasks and the tasks
        year.set(p[0], {'nrTotal': allItems[0], 'categories': allItems.slice(1)});
    }
    const returnData = {'summary':{ 'nrTotal': totalTaskCount}, year}
    return returnData;    
}