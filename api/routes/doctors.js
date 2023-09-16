const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt')
const {Doctor} = require('../models/doctor');

router.get('/',async (req,res)=>{
    let filter = {};
    if(req.query.speciality){
        filter  = {speciality: req.query.speciality};
    }
    const doctorsList = await Doctor.find(filter);
    if(!doctorsList){
        return res.status(500).json({success: false, message: 'Server error'});
    }
    res.status(200).send(doctorsList);
});

router.post('/',async (req,res)=>{
    try{
        let doctor = new Doctor({
            first_name : req.body.first_name,
            last_name : req.body.last_name,
            gender : req.body.gender,
            date_of_birth : req.body.date_of_birth,
            email : req.body.email,
            password : bcrypt.hashSync(req.body.password,10),
            phone : req.body.phone,
            address : {
                street : req.body.street,
                city : req.body.city,
                state : req.body.state,
                zip : req.body.zip
            },
            speciality : req.body.speciality,
            qualifications : req.body.qualifications,
            work_schedule : {
                days_of_week : req.body.days_of_week,
                start_time : req.body.start_time,
                end_time : req.body.end_time
            },
            is_active : req.body.is_active
        });
        doctor = await doctor.save();
        if(!doctor){
           return res.status(500).json({success: false, message: 'Doctor cannot be added'}); 
        }
        res.status(201).json({success: true, message: "Doctor Added"});
    }catch(e){
        res.status(500).json({success: false, message: e});
    }
});

module.exports = router;