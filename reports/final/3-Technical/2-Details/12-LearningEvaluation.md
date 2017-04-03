
#### Algorithm Evaluation {-}

In this section, we will discuss the scope of the learning our system is able to perform and how
well the different versions of the algorithm are able to learn behaviours. 

##### Scope {-}

The system is able to infer simple rules in which an action is triggered by a single event. The 
system can only associate the exact events with actions, two similar events will not trigger the 
same action. The system is not able to learn more complex behaviours in which a sequence or a 
combination of events trigger an action or sequence of actions. For example, the system is able
to learn to turn a light on after a motion event. However, it is not able to learn how to turn on
the light if the luminance level in the room is below a threshold. Another example of a behaviour
that the system would not be able to learn is to turn the light on in response to a combination of 
a motion event and a  window closing event.

#### Algorithm Performance {-}
 
To test how well the different algorithms performed each algorithm was trained to perform a set of 
behaviours using training data collected from the [Demo](#sec-3-2-15-1) environment. Each algorithm
was trained using the exact same training data, and each behaviour was tested independently. In each 
case a specific event-action pair was identified as the desired behaviour to be learned.

Two metrics were collected using the decision tables of the algorithms after they had been trained. 
The decision tables contain all of the event-action pairs that the system has learned. Any action in
this table will be performed when the corresponding event is observed. The first metric is whether 
or not the desired behaviour was learned. The second metric is the number of behaviours other than 
the desired behaviour that were learned. Table {Tnum} shows the results of the testing.


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


From the table, we can see that version 2 was clearly the worst performing strategy as it was only 
able to learn four of nine behaviours. Of the four it learned, it only learned one without learning 
any additional incorrect behaviours. Version 3 is an improvement on version 2 as it was able to learn 
all nine behaviours, however, it was only able to learn two of these behaviours without learning any
additional incorrect behaviours. Version 4 is clearly the best strategy as it was able to learn all 
of the behaviours and it learned five out of the nine without any incorrect behaviours.

An additional observation that can be made about the difference between version 3 and version 4
is that undesired behaviours learned by version 4 can be unlearned through additional, negative, 
training sessions. Table {reference} illustrates that the number of incorrect decisions made by 
version 4 can be reduced by performing additional training sessions, whereas additional training 
sessions have no effect or have a worsening effect when version 3 is used.

<br/>

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext 1.5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0in 5.4pt 0in 5.4pt;mso-border-insideh:
 1.5pt solid windowtext;mso-border-insidev:1.5pt solid windowtext'>
 <tr style='height:57.35pt'>
  <td width=186 style='width:139.25pt;border:solid windowtext 1.0pt;padding:
  0in 5.4pt 0in 5.4pt;height:57.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Behavior</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:solid windowtext 1.0pt;border-left:
  none;padding:0in 5.4pt 0in 5.4pt;height:57.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Session</span></p>
  </td>
  <td width=122 nowrap style='width:91.85pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt;height:57.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Version 3</span></p>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Number Wrong</span></p>
  </td>
  <td width=122 nowrap style='width:91.85pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt;height:57.35pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Version 4</span></p>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Number Wrong</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 rowspan=3 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Light on
  after motion</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F5B78D;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>5</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F5B78D;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>5</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 rowspan=3 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Light off
  after no motion</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F7C6A4;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>4</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 rowspan=4 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Orange Light
  on Pause</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F7C6A4;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>4</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F5B78D;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>5</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>4</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 nowrap rowspan=2 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Green on Play</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F3A976;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>6</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 nowrap rowspan=3 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Red on Stop</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#ED7D31;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>9</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F3A976;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>6</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 nowrap rowspan=7 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Window Open
  Light Off</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>4</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>5</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>6</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>7</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 nowrap rowspan=5 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Window Close
  Light On</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>4</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#FBE3D2;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>5</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 rowspan=2 style='width:139.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Light on
  after motion 2</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F9D4BB;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>3</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=186 nowrap rowspan=2 valign=bottom style='width:139.25pt;
  border:solid windowtext 1.0pt;border-top:none;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>Light off on
  no motion 2</span></p>
  </td>
  <td width=59 style='width:44.05pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:white;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border:none;
  border-right:solid windowtext 1.0pt;background:#F7C6A4;padding:0in 5.4pt 0in 5.4pt;
  height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>4</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=59 style='width:44.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>2</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:white;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>0</span></p>
  </td>
  <td width=122 nowrap valign=bottom style='width:91.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FDF1E9;padding:0in 5.4pt 0in 5.4pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black'>1</span></p>
  </td>
 </tr>
</table>

While version 4 has a lower rate of incorrect decisions than any previous version, it does still 
learn incorrect behaviours. Unlearning some of these incorrect behaviours could be difficult or 
impossible due to the infrequency of the triggering action. For example, if an incorrect behaviour is 
triggered off a temperature of exactly 70.0999984741211 it is unlikely that this precise 
temperature will be observed frequently enough to unlearn the behaviour. One future enhancement that
could be made to the algorithm is the discretization of device data. Discretization of the data 
could increase the frequency of these events by treating groups of close values as the same event. 
For example, the system might consider any temperature in a range of 1 degree to be the same event.
This would allow incorrect behaviours to be unlearned by decreasing the number of infrequent events
observed during training sessions.