function getPathWithLangParam(to) {
  return to + window.location.search
}

function pageTitle(title) {
  return title ? `YouMeZurich - ${title}` : 'YouMeZurich'
}

// function getCurrentDayString() {
//   const weekdays = {
//     0: 'sunday',
//     1: 'monday',
//     2: 'tuesday',
//     3: 'wednesday',
//     4: 'thursday',
//     5: 'friday',
//     6: 'saturday'
//   }
//   const date = new Date()
//   return weekdays[date.getDay()]
// }

export { getPathWithLangParam, pageTitle, getCurrentDayString }
