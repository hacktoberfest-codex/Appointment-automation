const express = require('express');
const router = express.Router();
const {Appointment} = require('../models/appointment');

router.get('/',async (req,res)=>{
    let filter = {};
    if(req.query.doctor){
        filter = {doctor: req.query.doctor}
    }
    if(req.query.patient){
        filter = {patient: req.query.patient}
    }
    const appointmentList = await Appointment.find(filter).populate('patient').populate('doctor');
    if(!appointmentList){
        return res.status(404).json({success: false, message: 'No appointments found'})
    }
    res.status(200).send(appointmentList);
});

router.post('/',async (req,res)=>{
    let appointment = new Appointment({
        patient : req.body.patient,
        date : req.body.date,
        doctor : req.body.doctor,
        status : req.body.status,
        priority : req.body.priority
    });
    appointment = await appointment.save();
    if(!appointment){
        return res.status(500).json({success: false,message: "Appoinment can't be created"})
    }
    res.status(201).json({success: true,message: 'Appointment created successfully'});
});

module.exports = router;