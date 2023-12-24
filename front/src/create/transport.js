export async function sendTasks(data) {
    const response = await fetch('http://localhost:8080/task', {
        method: 'POST',
        body: getSendTasksRequestModel(data),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    console.log(response);
}

function getSendTasksRequestModel(check) {
    const requestModel = check.themes
        .filter(element => element.isVisible)
        .map(element => ({
            title: element.title,
            complexity: +element.selectedComplexity,
            count: +element.count || 1
        }));
    return JSON.stringify(requestModel);
}


