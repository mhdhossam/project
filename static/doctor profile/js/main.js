// var date=new Date();
// var year=new Date().getFullYear();
// var month=new Date().getMonth();
// var todayDate=String(date.getDate()).padStart(2, '0');
// var datepattern=year + '-' + month + '-' +todayDate;
// document.getElementById("date-picker").value=datepattern;

// calender
const date = new Date();

const renderCalendar = () => {
  date.setDate(1);

  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  const nextDays = 7 - lastDayIndex - 1;

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  document.querySelector(".date h1").innerHTML = months[date.getMonth()];

  document.querySelector(".date p").innerHTML = new Date().toDateString();

  let days = "";

  for (let x = firstDayIndex; x > 0; x--) {
    days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
  }

  for (let i = 1; i <= lastDay; i++) {
    if (
      i === new Date().getDate() &&
      date.getMonth() === new Date().getMonth()
    ) {
      days += `<div class="today">${i}</div>`;
    } else {
      days += `<div>${i}</div>`;
    }
  }

  for (let j = 1; j <= nextDays; j++) {
    days += `<div class="next-date">${j}</div>`;
    monthDays.innerHTML = days;
  }
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();

// End cLender

// Start select btn







var button = document.getElementsByClassName("button");
var addSelectClass = function m1() {
removeSelectClass();
this.classList.add("selected");
};


var removeSelectClass = function m1 () {
for (var i = 0; i < button.length; i++) {
    button[i].classList.remove("selected");
}
};

for (var i = 0; i < button.length; i++) {
button[i].addEventListener("click", addSelectClass);
}


var button1 = document.getElementsByClassName("button1");
var addSelectClass1 = function () {
removeSelectClass1();
this.classList.add("selected1");
};


var removeSelectClass1 = function () {
for (var i = 0; i < button1.length; i++) {
    button1[i].classList.remove("selected1");
}
};

for (var i = 0; i < button1.length; i++) {
button1[i].addEventListener("click", addSelectClass1);
}






// End select btn
