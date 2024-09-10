// Let's Design An Incremental Build System That Works With Files On A Storage Disk. • This Build System Will Consist Of One Or



function tasksToRun(taskDefinitionsInput, changedFiles) {
    // Write your code here
    let changedTask = []
   let files = taskDefinitionsInput.filter(files => files.includes("files"))
   let task= taskDefinitionsInput.filter(task => task.includes("task:"))
   let deps= taskDefinitionsInput.filter(task => task.includes("deps:"))
    console.log(files)
    console.log(changedFiles)
    console.log(deps)
    for(let i = 0; i < files.length; i++){
        for(let j = 0; j < changedFiles.length; j++){
            if(files[i].includes(changedFiles[j])){
                console.log("changed", task[i])
                changedTask.push(task[i].replace("task: " , ""))
            }
        }
    }
    return changedTask
}

console.log(tasksToRun([
    "task: taskA",
    "files: lib/foo.txt lib/bar.txt",
    "deps:",
    "",
    "task: taskB",
    "files: src/baz.txt",
    "deps:",
    "",
    "task: taskC",
    "files: README.md",
    "deps:",
    ""
  ],[
    "lib/foo.txt",
    "README.md"
  ]))
