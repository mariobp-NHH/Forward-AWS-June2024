const { useState, useEffect } = React;
const WeatherApp = () => {
  const [data, setData] = useState({});
  const [location, setLocation] = useState("");
  const [coords, setCoords] = useState(null);
  const api_key = "7dfae1c0be3358dd8cdb563483cb8881";
  useEffect(() => {
    const fetchDefaultWeather = async () => {
      try {
        const resLoc = await fetch("https://ipapi.co/json/");
        const locData = await resLoc.json();
        const lat = locData.latitude || 60.3913;
        const lon = locData.longitude || 5.3221;
        setCoords({
          lat,
          lon,
        });
        const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${api_key}&units=metric`;
        const res = await fetch(url);
        const defaultData = await res.json();
        setData(defaultData);
      } catch (error) {
        console.error("Error fetching weather:", error);
      }
    };
    fetchDefaultWeather();
  }, []);
  const handleInputChange = (e) => setLocation(e.target.value);
  const search = async () => {
    if (location.trim() !== "") {
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&units=metric&appid=${api_key}`;
      const res = await fetch(url);
      const searchData = await res.json();
      if (searchData.cod !== 200) {
        setData({
          notFound: true,
        });
      } else {
        setData(searchData);
        setLocation("");
      }
    }
  };
  const handleKeyDown = (e) => {
    if (e.key === "Enter") search();
  };
  const weatherImages = {
    Clear: "/static/icons/weather/sunny.png",
    Clouds: "/static/icons/weather/cloudy.png",
    Rain: "/static/icons/weather/rainy.png",
    Snow: "/static/icons/weather/snowy.png",
    Haze: "/static/icons/weather/cloudy.png",
    Mist: "/static/icons/weather/cloudy.png",
  };
  const weatherImage = data.weather
    ? weatherImages[data.weather[0].main]
    : null;
  const backgroundImages = {
    Clear: "linear-gradient(to right, #f3b07c, #fcd283)",
    Clouds: "linear-gradient(to right, #57d6d4, #71eeec)",
    Rain: "linear-gradient(to right, #5bc8fb, #80eaff)",
    Snow: "linear-gradient(to right, #aff2ff, #fff)",
    Haze: "linear-gradient(to right, #57d6d4, #71eeec)",
    Mist: "linear-gradient(to right, #57d6d4, #71eeec)",
  };
  const backgroundImage = data.weather
    ? backgroundImages[data.weather[0].main]
    : "linear-gradient(to right, #f3b07c, #fcd283)";
  const currentDate = new Date();
  const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  const months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const formattedDate = `${
    daysOfWeek[currentDate.getDay()]
  }, ${currentDate.getDate()} ${months[currentDate.getMonth()]}`;
  return /*#__PURE__*/ React.createElement(
    "div",
    {
      className: "container_weather",
      style: {
        backgroundImage,
      },
    },
    /*#__PURE__*/ React.createElement(
      "div",
      {
        className: "weather-app",
        style: {
          backgroundImage: backgroundImage.replace("to right", "to top"),
        },
      },
      /*#__PURE__*/ React.createElement(
        "div",
        {
          className: "search",
        },
        /*#__PURE__*/ React.createElement(
          "div",
          {
            className: "search-top",
          },
          /*#__PURE__*/ React.createElement("i", {
            className: "fa-solid fa-location-dot",
          }),
          /*#__PURE__*/ React.createElement(
            "div",
            {
              className: "location",
            },
            data.name
          )
        ),
        /*#__PURE__*/ React.createElement(
          "div",
          {
            className: "search-bar",
          },
          /*#__PURE__*/ React.createElement("input", {
            type: "text",
            placeholder: "Enter Location",
            value: location,
            onChange: handleInputChange,
            onKeyDown: handleKeyDown,
          }),
          /*#__PURE__*/ React.createElement("i", {
            className: "fa-solid fa-magnifying-glass",
            onClick: search,
          })
        )
      ),
      data.notFound
        ? /*#__PURE__*/ React.createElement(
            "div",
            {
              className: "not-found",
            },
            "Not found \uD83D\uDE29"
          )
        : /*#__PURE__*/ React.createElement(
            React.Fragment,
            null,
            /*#__PURE__*/ React.createElement(
              "div",
              {
                className: "weather",
              },
              weatherImage &&
                /*#__PURE__*/ React.createElement("img", {
                  src: weatherImage,
                  alt: "weather",
                }),
              /*#__PURE__*/ React.createElement(
                "div",
                {
                  className: "weather-type",
                },
                data.weather?.[0]?.main
              ),
              /*#__PURE__*/ React.createElement(
                "div",
                {
                  className: "temp",
                },
                data.main ? `${Math.floor(data.main.temp)}°` : null
              )
            ),
            /*#__PURE__*/ React.createElement(
              "div",
              {
                className: "weather-date",
              },
              /*#__PURE__*/ React.createElement("p", null, formattedDate)
            ),
            /*#__PURE__*/ React.createElement(
              "div",
              {
                className: "weather-data",
              },
              /*#__PURE__*/ React.createElement(
                "div",
                {
                  className: "humidity",
                },
                /*#__PURE__*/ React.createElement(
                  "div",
                  {
                    className: "data-name",
                  },
                  "Humidity"
                ),
                /*#__PURE__*/ React.createElement("i", {
                  className: "fa-solid fa-droplet",
                }),
                /*#__PURE__*/ React.createElement(
                  "div",
                  {
                    className: "data",
                  },
                  data.main?.humidity,
                  "%"
                )
              ),
              /*#__PURE__*/ React.createElement(
                "div",
                {
                  className: "wind",
                },
                /*#__PURE__*/ React.createElement(
                  "div",
                  {
                    className: "data-name",
                  },
                  "Wind"
                ),
                /*#__PURE__*/ React.createElement("i", {
                  className: "fa-solid fa-wind",
                }),
                /*#__PURE__*/ React.createElement(
                  "div",
                  {
                    className: "data",
                  },
                  data.wind?.speed,
                  " km/h"
                )
              )
            )
          )
    )
  );
};
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(/*#__PURE__*/ React.createElement(WeatherApp, null));
