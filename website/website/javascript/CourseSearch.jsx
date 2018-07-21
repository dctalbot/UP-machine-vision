/*
 * @flow
 */

import React from 'react'
import styled from 'styled-components'
import { Button, MenuItem } from '@blueprintjs/core'
import { Select } from '@blueprintjs/select'

import type { Course } from 'models'

const Container = styled.div`
  text-align: center;
`

const courseFilter = (query, item) => {
  return (
    `${item.COURSE_TITLE.toLowerCase()} ${item.COE_HOME_SUBJECT.toLowerCase()} ${
      item.CATALOG_NUMBER
    }`.indexOf(query.toLowerCase()) >= 0
  )
}

type Props = { handleClick: any }
type State = { courses: [] }

class CourseSearch extends React.Component<Props, State> {
  constructor() {
    super()

    this.state = {
      courses: []
    }
  }

  getCourses() {
    fetch(window.location + '/courses.json')
      .then(response => response.json())
      .then(responseJson => {
        this.setState({ courses: responseJson })
      })
      .catch(error => {
        console.error(error)
      })
  }

  itemRenderer(item: Course, props: Props) {
    return (
      <MenuItem
        key={item.URL}
        label={item.COE_HOME_SUBJECT + ' ' + item.CATALOG_NUMBER}
        text={item.COURSE_TITLE}
        shouldDismissPopover={true}
        onClick={props.handleClick}
      />
    )
  }

  onItemSelect(item: Course) {
    window.location = item.URL
  }

  componentDidMount() {
    this.getCourses()
  }

  render() {
    return (
      <Select
        items={this.state.courses}
        itemRenderer={this.itemRenderer}
        onItemSelect={this.onItemSelect}
        filterable={true}
        itemPredicate={courseFilter}
      >
        <Button text={'Search for a Course'} rightIcon="caret-down" />
      </Select>
    )
  }
}
export default CourseSearch
