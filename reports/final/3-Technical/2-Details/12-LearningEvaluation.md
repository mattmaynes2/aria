------------------------------
#### Algorithm Evaluation {-}

In this section we will discus the scope of the learning our system is able to perform and how
well the different versions of the algorithm are able to learn behaviours. 

##### Scope {-}

The system is able to infer simple rules in which an action is triggered by a single event. The 
system can only associate the exact events with actions, two similar events will not trigger the 
same action.The //TODO reword
system is not able to learn more complex behaviours in which a sequence or a combination of events 
trigger an action or sequence of actions. 

#### Algorithm Performance {-}
 
To test how well the different algorithms performed each algorithm was trained to perform a set of 
behaviours using training data collected from the [Demo](#sec-3-2-15-1) environment. Each algorithm
was trained using the exact same training data, and each behaviour was tested independently. In each 
case a specific event-action pair was identified as the desired behaviour to be learned.

Two metrics were collected using the decision tables of the algorithms after they had been trained. 
The decision tables contain all of the event-action pairs that the system has learned. Any action in
this table will be performed when the corresponding event is observed. The first metric is whether 
or not the desired behaviour was learned. The second metric is the number of behaviours other than 
the desired behaviour that were learned. 



For the 4th version of the algorithms different behaviours does not cause  
Trained using behaviour and session data used in the 
-	  
-	From table, we can see that version 2 was only able to learn 4 of 9 behaviours 
-	Of the 4 it learned it only learned 1 without any wrong decisions.
-	Version 3 learned all 9 behaviours but only learned 2 without any wrong decisions
-	Version 4 learned all behaviours and learned 5 of 9 without any wrong behaviours.
 

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext 1.5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0in 5.4pt 0in 5.4pt;mso-border-insideh:
 1.5pt solid windowtext;mso-border-insidev:1.5pt solid windowtext'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:12.0pt'>
  <td width=168 rowspan=2 style='width:125.75pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:12.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Behaviour<o:p></o:p></span></p>
  </td>
  <td width=152 nowrap colspan=2 valign=bottom style='width:113.9pt;border:
  solid windowtext 1.0pt;border-left:none;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:12.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Version 2<o:p></o:p></span></p>
  </td>
  <td width=152 nowrap colspan=2 valign=bottom style='width:113.9pt;border:
  solid windowtext 1.0pt;border-left:none;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:12.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Version 3<o:p></o:p></span></p>
  </td>
  <td width=152 nowrap colspan=2 valign=bottom style='width:113.95pt;
  border:solid windowtext 1.0pt;border-left:none;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:12.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Version 4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:15.0pt'>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Learned<o:p></o:p></span></p>
  </td>
  <td width=76 valign=bottom style='width:56.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Wrong Decisions<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Learned<o:p></o:p></span></p>
  </td>
  <td width=76 valign=bottom style='width:56.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Wrong Decisions<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Learned<o:p></o:p></span></p>
  </td>
  <td width=76 valign=bottom style='width:57.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Wrong Decisions<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:15.0pt'>
  <td width=168 style='width:125.75pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Light on after motion<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F9CFB3;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>1<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F29F66;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#EB6E19;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;height:14.35pt'>
  <td width=168 style='width:125.75pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:14.35pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Light off after no motion<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:14.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>N<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F29F66;padding:0in 5.4pt 0in 5.4pt;
  height:14.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:14.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F9CFB3;padding:0in 5.4pt 0in 5.4pt;
  height:14.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>1<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:14.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:14.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4;height:15.0pt'>
  <td width=168 nowrap valign=bottom style='width:125.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Orange Light on Pause<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>N<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#EB6E19;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>3<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#EB6E19;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>3<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5;height:15.0pt'>
  <td width=168 nowrap style='width:125.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Green on Play<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>N<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F29F66;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F29F66;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F9CFB3;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>1<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6;height:15.0pt'>
  <td width=168 nowrap style='width:125.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Red on Stop<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>N<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F29F66;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F29F66;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F29F66;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>2<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7;height:15.0pt'>
  <td width=168 nowrap style='width:125.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Window Open Light Off<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F9CFB3;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>1<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#EB6E19;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>3<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8;height:15.0pt'>
  <td width=168 nowrap style='width:125.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Window Close Light On<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F9CFB3;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>1<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#EB6E19;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>3<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9;height:15.0pt'>
  <td width=168 nowrap valign=bottom style='width:125.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Light on after motion 2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:10;mso-yfti-lastrow:yes;height:15.0pt'>
  <td width=168 nowrap valign=bottom style='width:125.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:Calibri;
  color:black'>Light off on no motion 2<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>N<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F9CFB3;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>1<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>0<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:56.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>Y<o:p></o:p></span></p>
  </td>
  <td width=76 nowrap valign=bottom style='width:57.0pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;background:#F9CFB3;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black'>1<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0
  style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext 1.5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0in 5.4pt 0in 5.4pt;mso-border-insideh:
 1.5pt solid windowtext;mso-border-insidev:1.5pt solid windowtext'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:15.0pt'>
  <td width=158  rowspan=2 style='width:118.75pt;border:solid windowtext 1.0pt;mso-border-alt:
  solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Behaviour<o:p></o:p></span></p>
  </td>
  <td width=59  rowspan=2 style='width:44.05pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Session<o:p></o:p></span></p>
  </td>
  <td width=147 nowrap colspan=2 valign=bottom style='width:110.35pt;
  border:solid windowtext 1.0pt;border-left:none;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Version 2<o:p></o:p></span></p>
  </td>
  <td width=147 nowrap colspan=2 valign=bottom style='width:110.35pt;
  border:solid windowtext 1.0pt;border-left:none;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Version 3<o:p></o:p></span></p>
  </td>
  <td width=147 nowrap colspan=2 valign=bottom style='width:110.35pt;
  border:solid windowtext 1.0pt;border-left:none;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Version 4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:30.0pt'>
  <td width=83 style='width:62.2pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:30.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Learned
  Behaviour<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:30.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Number
  wrong<o:p></o:p></span></p>
  </td>
  <td width=80 style='width:59.85pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:30.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Learned
  Behaviour<o:p></o:p></span></p>
  </td>
  <td width=67 style='width:50.5pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:30.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Number
  Wrong <o:p></o:p></span></p>
  </td>
  <td width=77 style='width:57.5pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:30.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Learned
  Behaviour<o:p></o:p></span></p>
  </td>
  <td width=70 style='width:52.85pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:30.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Number
  Wrong <o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:15.0pt'>
  <td width=158 rowspan=3 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Light on
  after motion<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  #F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F5B78D;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>5<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F5B78D;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>5<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5;height:15.0pt'>
  <td width=158 rowspan=3 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Light off
  after no motion<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F7C6A4;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:red;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8;height:15.0pt'>
  <td width=158 rowspan=4 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Orange
  Light on Pause<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F3A976;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  #F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F7C6A4;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:red;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F3A976;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:10;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:red;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#ED7D31;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F5B78D;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>5<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:11;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>4<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:12;height:15.0pt'>
  <td width=158 nowrap rowspan=2 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Green on
  Play<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F3A976;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  #F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>6<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:13;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:14;height:15.0pt'>
  <td width=158 nowrap rowspan=3 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Red on Stop<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F3A976;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  #F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>9<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:15;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:red;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F3A976;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>6<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:16;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F3A976;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:17;height:15.0pt'>
  <td width=158 nowrap rowspan=7 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Window Open
  Light Off<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:18;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:19;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:20;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>4<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:21;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>5<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:22;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>6<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:23;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>7<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:24;height:15.0pt'>
  <td width=158 nowrap rowspan=5 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Window
  Close Light On<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:25;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:26;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:27;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>4<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  #ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:28;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>5<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#ED7D31;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:29;height:15.0pt'>
  <td width=158 nowrap rowspan=3 style='width:118.75pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Light on
  after motion 2<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:red;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  red;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:30;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-right-alt:solid windowtext .5pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-left-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;background:
  white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-left-alt:
  solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;height:
  15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:31;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>3<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:lime;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:32;height:15.0pt'>
  <td width=158 nowrap rowspan=2 valign=bottom style='width:118.75pt;
  border:solid windowtext 1.0pt;border-top:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Light off
  on no motion 2<o:p></o:p></span></p>
  </td>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;mso-border-top-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border:none;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border:none;border-right:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;background:
  white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border:none;
  border-right:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F7C6A4;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:33;mso-yfti-lastrow:yes;height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>2<o:p></o:p></span></p>
  </td>
  <td width=83 style='width:62.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;background:red;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>N<o:p></o:p></span></p>
  </td>
  <td width=64 style='width:48.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
  <td width=80 nowrap valign=bottom style='width:59.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-left-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  background:lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=67 nowrap valign=bottom style='width:50.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>0<o:p></o:p></span></p>
  </td>
  <td width=77 nowrap valign=bottom style='width:57.5pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-left-alt:solid windowtext .5pt;mso-border-left-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;background:
  lime;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>Y<o:p></o:p></span></p>
  </td>
  <td width=70 nowrap valign=bottom style='width:52.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-CA style='mso-ascii-font-family:
  Calibri;mso-fareast-font-family:"Times New Roman";mso-hansi-font-family:Calibri;
  mso-bidi-font-family:Calibri;color:black;mso-ansi-language:EN-CA'>1<o:p></o:p></span></p>
  </td>
 </tr>
</table>