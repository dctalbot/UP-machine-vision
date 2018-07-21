/**
 * @providesModule Course
 * @flow
 */

export type Course = {
  +CATALOG_NUMBER: number,
  +COE_HOME_SUBJECT: string,
  +COURSE_TITLE: string,
  +URL: string
}

export const defaultCourse: Course = {
  CATALOG_NUMBER: 0,
  COE_HOME_SUBJECT: '',
  COURSE_TITLE: '',
  URL: ''
}
