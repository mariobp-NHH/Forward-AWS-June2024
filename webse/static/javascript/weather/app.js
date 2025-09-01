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
        setCoords({ lat, lon });

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

  const handleInputChange = (event) => setLocation(event.target.value);

  const search = async () => {
    if (location.trim() !== "") {
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&units=metric&appid=${api_key}`;
      const res = await fetch(url);
      const searchData = await res.json();
      if (searchData.cod !== 200) {
        setData({ notFound: true });
      } else {
        setData(searchData);
        setLocation("");
      }
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") search();
  };

  const weatherImages = {
    Clear: "/static/figures/gd_course/weather/sunny.png",
    Clouds: "/static/figures/gd_course/weather/cloudy.png",
    Rain: "/static/figures/gd_course/weather/rainy.png",
    Snow: "/static/figures/gd_course/weather/snowy.png",
    Haze: "/static/figures/gd_course/weather/cloudy.png",
    Mist: "/static/figures/gd_course/weather/cloudy.png",
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

  return (
    <div className="container_weather" style={{ backgroundImage }}>
      <div
        className="weather-app"
        style={{
          backgroundImage: backgroundImage.replace("to right", "to top"),
        }}
      >
        <div className="search">
          <div className="search-top">
            <i className="fa-solid fa-location-dot"></i>
            <div className="location">{data.name}</div>
          </div>
          <div className="search-bar">
            <input
              type="text"
              placeholder="Enter Location"
              value={location}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
            />
            <i className="fa-solid fa-magnifying-glass" onClick={search}></i>
          </div>
        </div>

        {data.notFound ? (
          <div className="not-found">Not found 😩</div>
        ) : (
          <>
            <div className="weather">
              {weatherImage && <img src={weatherImage} alt="weather" />}
              <div className="weather-type">{data.weather?.[0]?.main}</div>
              <div className="temp">
                {data.main ? `${Math.floor(data.main.temp)}°` : null}
              </div>
            </div>
            <div className="weather-date">
              <p>{formattedDate}</p>
            </div>
            <div className="weather-data">
              <div className="humidity">
                <div className="data-name">Humidity</div>
                <i className="fa-solid fa-droplet"></i>
                <div className="data">{data.main?.humidity}%</div>
              </div>
              <div className="wind">
                <div className="data-name">Wind</div>
                <i className="fa-solid fa-wind"></i>
                <div className="data">{data.wind?.speed} km/h</div>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<WeatherApp />);
