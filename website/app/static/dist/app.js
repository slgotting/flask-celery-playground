function addToScore(){console.log(gameSocket);gameSocket.emit('add_to_score',{'he':'test','there':'t2'})}
let hideNotification;function showNotification(resultObject){if(hideNotification){clearTimeout(hideNotification);}
let div=document.getElementById('notification_div');div.style.display='block';div.style.background=resultObject.type=="success"?"green":"red";div.innerText=resultObject.message;hideNotification=setTimeout(()=>{div.style.display='none';},5000);}
let queueTimerInterval;function startQueueTimer(timeInQueue){let outerDiv=document.getElementById('queue-timer');outerDiv.style.display='block';let div=document.getElementById('queue-timer-count');div.innerText=timeInQueue;queueTimerInterval=setInterval(()=>{div.innerText=parseInt(div.innerText)+1;},1000);}
function endQueueTimer(){let outerDiv=document.getElementById('queue-timer');outerDiv.style.display='none';clearInterval(queueTimerInterval);}