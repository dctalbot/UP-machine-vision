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

  onDrop(files) {
    this.setState({
      files: files
    });

    var XHR = new XMLHttpRequest();
    var FD = new FormData();

    // Push our data into our FormData object
    FD.append("file", files[0]);
    // FD.append("filename", files[0].value);

    // Set up our request
    XHR.open("POST", "/");

    // Send our FormData object; HTTP headers are set automatically
    XHR.send(FD);

    XHR.onreadystatechange = function() {
      window.location = "/" + files[0].name;
    };
  }

  render() {
    return (
      <Container>
        <FormGroup
          helperText="Your image will be classified upon upload"
          labelFor="text-input"
          labelInfo="(required)"
        >
          <Dropzone onDrop={this.onDrop.bind(this)} className={"dropzone"}>
            <DropzoneText>{"Upload an Image..."}</DropzoneText>
          </Dropzone>
        </FormGroup>
      </Container>
    );
  }
}

// <Select
//   items={[{ name: "Springs" }, { name: "Wheels" }, { name: "Brakes" }]}
//   itemRenderer={this.itemRenderer}
//   onItemSelect={this.onItemSelect.bind(this)}
//   filterable={false}
// >
//   <Button text={this.state.selected} rightIcon="caret-down" />
// </Select>

// {"Upload " + this.state.selected.slice(0, -1) + " Image..."}
