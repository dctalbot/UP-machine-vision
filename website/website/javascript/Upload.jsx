import React from "react";
import styled from "styled-components";
import Dropzone from "react-dropzone";

import { RadioGroup, Radio, Button, MenuItem, FormGroup, FileInput } from "@blueprintjs/core";
import { Select } from "@blueprintjs/select";

const Container = styled.div`
  text-align: center;
`;

const List = styled.ul`
  text-align: left;
`;

const DropzoneText = styled.p`
  color: black;
  margin-top: 50px;
`;

export default class Upload extends React.Component {
  constructor() {
    super();

    this.state = {
      selected: "Springs",
      file: []
    };
  }

  itemRenderer(item, props) {
    return (
      <MenuItem
        key={item.name}
        label={item.name}
        text={item.name}
        shouldDismissPopover={true}
        onClick={props.handleClick}
      />
    );
  }

  onItemSelect(item) {
    console.log(this);
    this.setState({ selected: item.name });
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);
    data.append("filename", this.fileName.value);

    fetch("http://localhost:5000/", {
      method: "POST",
      body: data
    });
  }

  post(path, params) {
    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", path);

    for (var key in params) {
      if (params.hasOwnProperty(key)) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
      }
    }

    document.body.appendChild(form);
    form.submit();
  }

  onDrop(files) {
    this.setState({
      files: files
    });

    // const data = new FormData();
    // data.append("file", files[0]);
    // data.append("filename", files[0].value);

    // fetch("http://localhost:5000/", {
    //   method: "POST",
    //   body: data
    // });

    // $.ajax({
    //   url: "/",
    //   type: "POST",
    //   data: data,
    //   processData: false,
    //   contentType: false,
    //   success: function(response) {
    //     console.log("success");
    //   },
    //   error: function(jqXHR, textStatus, errorMessage) {
    //     console.log(errorMessage); // Optional
    //   }
    // });

    var XHR = new XMLHttpRequest();
    var FD = new FormData();

    // Push our data into our FormData object
    FD.append("file", files[0]);
    FD.append("filename", files[0].value);

    // Define what happens on successful data submission
    // XHR.addEventListener("load", function(event) {
    //   alert("Yeah! Data sent and response loaded.");
    // });
    //
    // // Define what happens in case of error
    // XHR.addEventListener("error", function(event) {
    //   alert("Oops! Something went wrong.");
    // });

    // Set up our request
    XHR.open("POST", "/");

    // Send our FormData object; HTTP headers are set automatically
    XHR.send(FD);
  }

  render() {
    return (
      <Container>
        <Select
          items={[{ name: "Springs" }, { name: "Wheels" }, { name: "Brakes" }]}
          itemRenderer={this.itemRenderer}
          onItemSelect={this.onItemSelect.bind(this)}
          filterable={false}
        >
          <Button text={this.state.selected} rightIcon="caret-down" />
        </Select>

        <FormGroup
          helperText="Your image will be classified upon upload"
          labelFor="text-input"
          labelInfo="(required)"
        >
          <Dropzone onDrop={this.onDrop.bind(this)} className={"dropzone"}>
            <DropzoneText>
              {"Upload " + this.state.selected.slice(0, -1) + " Image..."}
            </DropzoneText>
          </Dropzone>
        </FormGroup>
      </Container>
    );
  }
}
