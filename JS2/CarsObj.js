let cars = {
    Toyota: {
      Camry: {
        color: "Silver",
        year: generateYears()
      },
      Corolla: {
        color: "Blue",
        year: 2021
      }
    },
    Honda: {
      Civic: {
        color: "Red",
        year: 2020
      },
      Accord: {
        color: "Black",
        year: 2023
      }
    }
  };
  
  function generateYears() {
    let start= 2023
    const years = [];
    for (let i = 1; i <= 10; i++) {
      years.push(start - i);
    }
    return years;
  }
  
  console.log(cars.Toyota.Camry.year);
  console.log(typeof cars.Toyota.Camry.color);
  
  