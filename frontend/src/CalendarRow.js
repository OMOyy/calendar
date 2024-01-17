import React from 'react'
import CalendarCell from './CalendarCell';
import 'bootstrap/dist/css/bootstrap.min.css';
const CalendarRow = () => {
  return (
    <>
    <div className='d-flex calendarRow'>
        <CalendarCell/>
        <CalendarCell/>
        <CalendarCell/>
        <CalendarCell/>
        <CalendarCell/>
        <CalendarCell/>
        <CalendarCell/>
    </div>
    
    </>
  )
}
export default CalendarRow