const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt')
const {Patient} = require('../models/patient');

router.get('/',async (req,res)=>{
    const patientList = await Patient.find();
    if(!patientList){
        return res.status(500).json({success: false, message: "Can't get list"});
    }
    res.status(200).send(patientList);
});

router.post('/',async (req,res)=>{
    try{
        let patient = new Patient({
            first_name : req.body.first_name,
            last_name : req.body.last_name,
            gender : req.body.gender,
            date_of_birth : req.body.date_of_birth,
            blood_group : req.body.blood_group,
            email : req.body.email,
            password : bcrypt.hashSync(req.body.password,10),
            phone : req.body.phone,
            address : {
                street : req.body.street,
                city : req.body.city,
                state : req.body.state,
                zip : req.body.zip
            },
            
        });
        patient = await patient.save();
        if(!patient){
           return res.status(500).json({success: false, message: 'Patient cannot be added'}); 
        }
        res.status(201).json({success: true, message: "Patient Added"});
    }catch(e){
        res.status(500).json({success: false, message: e});
    }
});

module.exports = router;