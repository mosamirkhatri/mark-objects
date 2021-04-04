import axios from "axios";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import { downloadBlob } from "../helpers";

const Report = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const onGetReport = async () => {
    if (startDate && endDate) {
      axios
        .post(
          "/api/report",
          { start_date: startDate, end_date: endDate },
          {
            responseType: "blob",
          }
        )
        .then((response) => {
          console.log(response);
          const filename = response.headers["content-disposition"].split(
            "filename="
          )[1];
          const { data } = response;
          downloadBlob(data, filename);
        });
    }
  };

  return (
    <div className={"report-wrapper"}>
      <Link className={"report-wrapper__upload-page-link"} to={"/"}>
        Upload
      </Link>
      <div className={"report-wrapper__input-wrapper"}>
        <section>
          <label>Start Date:</label>
          <input
            value={startDate}
            type="date"
            onChange={(e) => setStartDate(e.target.value)}
          />
        </section>
        <section className={"report-wrapper__end-date-wrapper"}>
          <label>End Date:</label>
          <input
            value={endDate}
            type="date"
            onChange={(e) => setEndDate(e.target.value)}
          />
        </section>
        <button className={"upload-wrapper__get-report"} onClick={onGetReport}>
          Get Report
        </button>
      </div>
    </div>
  );
};

export default Report;
