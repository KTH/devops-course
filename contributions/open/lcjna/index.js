google.charts.load('current', { packages: ['corechart'] });
google.charts.setOnLoadCallback(drawChart);
function drawChart(offlineAmount) {
  if (offlineAmount === undefined) {
    offlineAmount = 0;
  }
  var data = google.visualization.arrayToDataTable([
    ['Status', 'Servers'],
    ['Online', 64 - offlineAmount],
    ['Offline', 0 + offlineAmount]
  ]);

  var options = {
    title: 'US-West Servers',
    pieHole: 0.4,
    colors: ['#8BC34A', '#F44336'],
    width: 512,
    height: 240,
    chartArea: {
      left: 20,
      top: 25,
      width: '100%',
      height: '80%'
    }
  };

  var chart = new google.visualization.PieChart(
    document.getElementById('donutchart')
  );
  chart.draw(data, options);
}

let messages = [
  {
    type: 'Commit',
    message: 'rebase patches to fix master build',
    status: 'Pending'
  },
  {
    type: 'Commit',
    message: 'rebase patches to fix master build',
    status: 'Accepted'
  },
  {
    type: 'Commit',
    message: 'Fix issue #1202',
    status: 'Pending'
  },
  {
    type: 'Commit',
    message: 'Fix issue #1202',
    status: 'Accepted'
  },
  {
    type: 'Server',
    message: 'US-West-28 has gone dark',
    status: 'Offline'
  },
  {
    type: 'Server',
    message: 'US-West-28 has rebooted',
    status: 'Online'
  },
  {
    type: 'Commit',
    message: 'remove useless variable declaration',
    status: 'Pending'
  },
  {
    type: 'Commit',
    message: 'remove useless variable declaration',
    status: 'Accepted'
  },
  {
    type: 'Commit',
    message: 'Document all the linemodes',
    status: 'Pending'
  },
  {
    type: 'Commit',
    message: 'Document all the linemodes',
    status: 'Accepted'
  },
  {
    type: 'Commit',
    message: 'Simplify the usage of :tag_toggle',
    status: 'Pending'
  },
  {
    type: 'Commit',
    message: 'Simplify the usage of :tag_toggle',
    status: 'Accepted'
  },
  {
    type: 'Commit',
    message: 'Add generational learning to servers',
    status: 'Pending'
  },
  {
    type: 'Commit',
    message: 'Add generational learning to servers',
    status: 'Accepted'
  }
];

let table = document.getElementById('tableBody');

let theTime = 1;
window.setInterval(function() {
  processTime(theTime++);
}, 500);

let clock = document.getElementById('clock');
let crashing = false;
// Set the table to have 12 empty rows.
for (let i = 0; i < 12; i++) {
  table.innerHTML += getEmptyRowHtml();
}

let serverActivity = document.getElementById('serverActivity');

for (let i = 0; i < 64; i++) {
  let serverNumber = i + 1 < 10 ? '0' + (i + 1) : i + 1;
  let buttonHtml =
    "<button type='button' class='btn btn-success' data-name='US-West-" +
    serverNumber +
    "' data-toggle='tooltip' data-placement='top' title='US-West-" +
    serverNumber +
    "'></button>";

  serverActivity.innerHTML += buttonHtml;
}

let buttons = $('.btn-success');

$(function() {
  $('[data-toggle="tooltip"]').tooltip();
});

function processTime(timestep) {
  if (buttons.length === 0 || timestep > 360) {
    // End it at 15:00 or earlier if all the servers died
    $('#modal').modal({ show: true });
    return;
  }

  updateClockTime(timestep);
  blinkSomeButtons();

  switch (timestep) {
    case 300:
      startKillingButtons();
      break;
    case 7:
    case 12:
    case 32:
    case 45:
    case 70:
    case 85:
    case 101:
    case 145:
    case 159:
    case 193:
    case 206:
    case 261:
    case 296:
      addMessageFromData(timestep);
      break;
    case 64:
      killOneButton();
      addMessageFromData(timestep);
      break;
  }

  if (crashing) {
    killButtons();
  }
}

function updateClockTime(timestep) {
  let hours = 9 + Math.floor(timestep / 60);
  let minutes = timestep % 60;

  if (hours < 10) {
    hours = '0' + hours;
  }
  if (minutes < 10) {
    minutes = '0' + minutes;
  }

  let time = hours + ':' + minutes;
  let clockHTML = '<h1>' + time + '</h1>';
  clock.innerHTML = clockHTML;
}
function killButtons() {
  let amountToKill = getRandomInteger(1, 5);

  if (buttons.length < amountToKill) {
    amountToKill = buttons.length;
  }

  let buttonsToKill = getRandomButtons(amountToKill);
  for (button of buttonsToKill) {
    button.classList.remove('btn-success');
    button.classList.add('btn-danger');

    let message = {
      type: 'Server',
      message: button.dataset.originalTitle + ' has gone dark',
      status: 'Offline'
    };

    addMessageToTable(message);
  }
  buttons = $('.btn-success');
  drawChart(64 - buttons.length);
}
function startKillingButtons() {
  crashing = true;
  killButtons();
}

function blinkSomeButtons() {
  let amountToBlink = getRandomInteger(1, 5);

  if (buttons.length < amountToBlink) {
    amountToBlink = buttons.length;
  }

  let buttonsToBlink = getRandomButtons(amountToBlink);

  for (button of buttonsToBlink) {
    if (button.classList.contains('btn-success')) {
      button.animate([{ opacity: 1 }, { opacity: 0.5 }, { opacity: 1 }], 500);
    }
  }
}

function killOneButton() {
  let buttonToKill = buttons[27];

  buttonToKill.classList.remove('btn-success');
  buttonToKill.classList.add('btn-danger');
  drawChart(1);
  setTimeout(function() {
    buttonToKill.classList.remove('btn-danger');
    buttonToKill.classList.add('btn-success');
    drawChart(0);
  }, 3000);
}

function getRandomButtons(amountToBlink) {
  let buttonsToBlink = [];

  if (buttons.length === 0) {
    return buttonsToBlink;
  }

  let indexes = [];

  for (let i = 0; i < amountToBlink; i++) {
    let randomIndex = getRandomInteger(0, buttons.length);

    // Ten tries to pick another number, was a while loop but this avoids infinite loops
    for (let j = 0; j < 10; j++) {
      if (indexes.indexOf(randomIndex) == -1) {
        break;
      }
      randomIndex = getRandomInteger(0, buttons.length);
    }

    indexes.push(randomIndex);
  }

  for (let i = 0; i < amountToBlink; i++) {
    buttonsToBlink.push(buttons[indexes[i]]);
  }

  return buttonsToBlink;
}

function getRandomInteger(min, max) {
  return Math.floor(Math.random() * (+max - +min)) + +min;
}

function addMessageFromData(timestep) {
  let message = messages[0];
  addMessageToTable(message);

  messages.splice(0, 1);
}

function addMessageToTable(message) {
  var rowCount = table.rows.length;
  table.deleteRow(rowCount - 1);

  let currentTime = document.getElementById('clock').innerText;
  let newRow = '<tr>';
  newRow += '<td>' + currentTime + '</td>';
  newRow += '<td>' + message.type + '</td>';
  newRow += '<td>' + message.message + '</td>';
  newRow += '<td>' + getHtmlBadgeFromText(message.status) + '</td>';
  newRow += '</tr>';
  table.innerHTML = newRow + table.innerHTML;
}

function getEmptyRowHtml() {
  return '<tr><td>&nbsp;</td><td></td><td></td><td></td></tr>';
}

function drawActivityTable(theTime) {
  table.innerHTML = '';
  for (var i = 0; i < theTime; i++) {
    let message = messages[i];
    let html = '<tr>';
    html += '<td>' + message.time + '</td>';
    html += '<td>' + message.type + '</td>';
    html += '<td>' + message.message + '</td>';
    html += '<td>' + getHtmlBadgeFromText(message.status) + '</td>';
    html += '</tr>';
    table.innerHTML = html + table.innerHTML;
  }
}
function getHtmlBadgeFromText(status) {
  if (status === 'Pending') {
    return "<span class='badge badge-info'>Pending</span>";
  } else if (status === 'Accepted') {
    return "<span class='badge badge-success'>Accepted</span>";
  } else if (status === 'Offline') {
    return "<span class='badge badge-danger'>Offline</span>";
  } else if (status === 'Online') {
    return "<span class='badge badge-success'>Online</span>";
  }
}

$('#addTests').on('click', function() {
  window.location.href = 'indexwithtests.html';
});

$('#watchAgain').on('click', function() {
  window.location.href = 'index.html';
});
