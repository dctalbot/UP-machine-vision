/**
 * @providesModule Subject
 * @flow
 */

export type Subject = {
  +COE_HOME_SUBJECT: string,
  +COE_HOME_SUBJECT_DESCRIPTION: string,
  +COE_HOME_SUBJECT_KEY: number,
  +URL: string
}

export const defaultSubject: Subject = {
  COE_HOME_SUBJECT: '',
  COE_HOME_SUBJECT_DESCRIPTION: '',
  COE_HOME_SUBJECT_KEY: 0,
  URL: ''
}
