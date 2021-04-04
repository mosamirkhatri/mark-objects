import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import { downloadBlob } from "../helpers";
import "./Upload.style.css";
import uploadImg from "../assets/upload.svg";

const Upload = () => {
  const [image, setImage] = useState({
    file: null,
    name: "",
    error: "",
  });

  const [xml, setXml] = useState({ file: null, name: "", error: "" });

  const onImageChoose = (e) => {
    console.log(e.target.files[0]);
    if (
      !(
        e.target.files[0].type === "image/jpeg" ||
        e.target.files[0].type === "image/jpg"
      )
    ) {
      setImage((prev) => ({
        name: "",
        file: null,
        error: "Please Choose a JPG File",
      }));
    }

    setImage((prev) => ({
      error: "",
      file: e.target.files[0],
      name: e.target.files[0].name,
    }));
  };

  const onXmlChoose = (e) => {
    console.log(e);
    console.log(e.target.files[0]);
    if (!(e.target.files[0].type === "text/xml")) {
      setXml((prev) => ({
        name: "",
        file: null,
        error: "Please Choose a xml File",
      }));
    }

    setXml((prev) => ({
      error: "",
      file: e.target.files[0],
      name: e.target.files[0].name,
    }));
  };

  const onUpload = async () => {
    if (image.file && xml.file) {
      let formData = new FormData();
      formData.append("image", image.file);
      formData.append("xml", xml.file);
      axios
        .post("/api/mark", formData, {
          responseType: "blob",
        })
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
    <div className={"upload-wrapper"}>
      <Link className={"upload-wrapper__report-page-link"} to={"/report"}>
        Report
      </Link>
      <div className={"upload-wrapper__input-wrapper"}>
        <section>
          <label htmlFor="image">
            <span>Upload Image File</span>
            <img src={uploadImg} alt={"upload"} />
            <input
              id={"image"}
              className={"upload-wrapper__image"}
              type={"file"}
              accept={".jpg"}
              onChange={onImageChoose}
            />
          </label>
          {image.error && (
            <p className={"upload-wrapper__error"}>{image.error}</p>
          )}
          {image.name && <p className={"upload-wrapper__name"}>{image.name}</p>}
        </section>
        <section className={"upload-wrapper__xml-wrapper"}>
          <label htmlFor="xml">
            <span>Upload XML File</span>
            <img src={uploadImg} alt={"upload"} />
            <input
              id={"xml"}
              className={"upload-wrapper__xml"}
              type={"file"}
              accept={".xml"}
              onChange={onXmlChoose}
            />
          </label>
          {xml.error && <p className={"upload-wrapper__error"}>{xml.error}</p>}
          {xml.name && <p className={"upload-wrapper__name"}>{xml.name}</p>}
        </section>
        <button className={"upload-wrapper__upload"} onClick={onUpload}>
          Upload
        </button>
      </div>
    </div>
  );
};

export default Upload;
