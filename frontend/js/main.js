// clock

function clockWeb (){
    const month = [
        'Januray','Februay','March','April','May','june','July','August','September','October','November','Devember'
    ]
    let d = new Date();
    let day = d.getDate();
    let year = d.getFullYear();
    let hour = d.getHours();
    let minute = d.getMinutes();
    let second = d.getSeconds();
    // let miSecond = d.getMilliseconds();

    let p = 'AM'
    if(hour > 12){
        hour = hour - 12
        p = 'PM'
    }

    if(hour < 10){
        hour = '0' + hour
    }
    if(minute < 10){
        minute = '0' + minute
    }
    if(second < 10){
        second = '0' + second
    }
    // if (miSecond < 100){
    //     miSecond = '0' + miSecond
    // }
    let clock = ` ${day} ${month[d.getMonth()]} ${year} ${hour}:${minute}:${second}`
    document.getElementById('MyClockDisplay').textContent = clock;

    setTimeout(clockWeb,1000);
}
clockWeb()