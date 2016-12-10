import sys
from pytest import fixture, mark
from subprocess import Popen, PIPE


@fixture
def comm_path(request):
    return 'tests/testdata/serif_dog-bites-man.concrete'


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\nconll\n-----\n'),
])
def test_print_conll_style_tags_for_communication(comm_path, args,
                                                  output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--char-offsets',
        '--dependency',
        '--lemmas',
        '--ner',
        '--pos',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
INDEX\tTOKEN\tCHAR\tLEMMA\tPOS\tNER\tHEAD\tDEPREL
-----\t-----\t----\t-----\t---\t---\t----\t------
1\tJohn\tJohn\t\tNNP\tPER\t\t
2\tSmith\tSmith\t\tNNP\tPER\t\t
3\t,\t,\t\t,\t\t\t
4\tmanager\tmanager\t\tNN\t\t\t
5\tof\tof\t\tIN\t\t\t
6\tACME\tACME\t\tNNP\tORG\t\t
7\tINC\tINC\t\tNNP\tORG\t\t
8\t,\t,\t\t,\t\t\t
9\twas\twas\t\tVBD\t\t\t
10\tbit\tbit\t\tNN\t\t\t
11\tby\tby\t\tIN\t\t\t
12\ta\ta\t\tDT\t\t\t
13\tdog\tdog\t\tNN\t\t\t
14\ton\ton\t\tIN\t\t\t
15\tMarch\tMarch\t\tDATE-NNP\t\t\t
16\t10th\t10th\t\tJJ\t\t\t
17\t,\t,\t\t,\t\t\t
18\t2013\t2013\t\tCD\t\t\t
19\t.\t.\t\t.\t\t\t

1\tHe\tHe\t\tPRP\t\t\t
2\tdied\tdied\t\tVBD\t\t\t
3\t!\t!\t\t.\t\t\t

1\tJohn\tJohn\t\tNNP\tPER\t\t
2\t's\t's\t\tPOS\t\t\t
3\tdaughter\tdaughter\t\tNN\t\t\t
4\tMary\tMary\t\tNNP\tPER\t\t
5\texpressed\texpressed\t\tVBD\t\t\t
6\tsorrow\tsorrow\t\tNN\t\t\t
7\t.\t.\t\t.\t\t\t

'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\nentities\n--------\n'),
])
def test_print_entities(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--entities',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
Entity Set 0 (Serif: doc-entities):
  Entity 0-0:
      EntityMention 0-0-0:
          tokens:     John Smith
          text:       John Smith
          entityType: PER
          phraseType: PhraseType.NAME
      EntityMention 0-0-1:
          tokens:     John Smith , manager of ACME INC ,
          text:       John Smith, manager of ACME INC,
          entityType: PER
          phraseType: PhraseType.APPOSITIVE
      EntityMention 0-0-2:
          tokens:     manager of ACME INC
          text:       manager of ACME INC
          entityType: PER
          phraseType: PhraseType.COMMON_NOUN
      EntityMention 0-0-3:
          tokens:     He
          text:       He
          entityType: PER
          phraseType: PhraseType.PRONOUN
      EntityMention 0-0-4:
          tokens:     John
          text:       John
          entityType: PER.Individual
          phraseType: PhraseType.NAME

  Entity 0-1:
      EntityMention 0-1-0:
          tokens:     ACME INC
          text:       ACME INC
          entityType: ORG
          phraseType: PhraseType.NAME

  Entity 0-2:
      EntityMention 0-2-0:
          tokens:     John 's daughter Mary
          text:       John's daughter Mary
          entityType: PER.Individual
          phraseType: PhraseType.NAME
      EntityMention 0-2-1:
          tokens:     daughter
          text:       daughter
          entityType: PER
          phraseType: PhraseType.COMMON_NOUN


Entity Set 1 (Serif: doc-values):
  Entity 1-0:
      EntityMention 1-0-0:
          tokens:     March 10th , 2013
          text:       March 10th, 2013
          entityType: TIMEX2.TIME
          phraseType: PhraseType.OTHER


'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\nsituation mentions\n------------------\n'),
])
def test_print_situation_mentions(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--situation-mentions',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
Situation Set 0 (Serif: relations):
  SituationMention 0-0:
          situationType:      ORG-AFF.Employment
          Argument 0:
              role:           Role.RELATION_SOURCE_ROLE
              entityMention:  manager of ACME INC
          Argument 1:
              role:           Role.RELATION_TARGET_ROLE
              entityMention:  ACME INC

  SituationMention 0-1:
          situationType:      PER-SOC.Family
          Argument 0:
              role:           Role.RELATION_SOURCE_ROLE
              entityMention:  John
          Argument 1:
              role:           Role.RELATION_TARGET_ROLE
              entityMention:  daughter


Situation Set 1 (Serif: events):
  SituationMention 1-0:
          text:               died
          situationType:      Life.Die
          Argument 0:
              role:           Victim
              entityMention:  He


'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\nsituations\n----------\n'),
])
def test_print_situations(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--situations',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
Situation Set 0 (Serif: relations):

Situation Set 1 (Serif: events):
  Situation 1-0:
      situationType:    Life.Die


'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\ntext\n----\n'),
])
def test_print_text_for_communication(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--text',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
<DOC id="dog-bites-man" type="other">
<HEADLINE>
Dog Bites Man
</HEADLINE>
<TEXT>
<P>
John Smith, manager of ACME INC, was bit by a dog on March 10th, 2013.
</P>
<P>
He died!
</P>
<P>
John's daughter Mary expressed sorrow.
</P>
</TEXT>
</DOC>

'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\nmentions\n--------\n'),
])
def test_print_tokens_with_entityMentions(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--mentions',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''
<ENTITY ID=0><ENTITY ID=0>John Smith</ENTITY> , <ENTITY ID=0>manager of \
<ENTITY ID=1>ACME INC</ENTITY></ENTITY> ,</ENTITY> was bit by a dog on \
<ENTITY ID=3>March 10th , 2013</ENTITY> .

<ENTITY ID=0>He</ENTITY> died !

<ENTITY ID=2><ENTITY ID=0>John</ENTITY> 's <ENTITY ID=2>daughter</ENTITY> \
Mary</ENTITY> expressed sorrow .

'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\ntokens\n------\n'),
])
def test_print_tokens_for_communication(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--tokens',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''
John Smith , manager of ACME INC , was bit by a dog on March 10th , 2013 .

He died !

John 's daughter Mary expressed sorrow .

'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\ntreebank\n--------\n'),
])
def test_print_penn_treebank_for_communication(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--treebank',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
(S (NP (NPP (NNP john)
            (NNP smith))
       (, ,)
       (NP (NPA (NN manager))
           (PP (IN of)
               (NPP (NNP acme)
                    (NNP inc))))
       (, ,))
   (VP (VBD was)
       (NP (NPA (NN bit))
           (PP (IN by)
               (NP (NPA (DT a)
                        (NN dog))
                   (PP (IN on)
                       (NP (DATE (DATE-NNP march)
                                 (JJ 10th))
                           (, ,)
                           (NPA (CD 2013))))))))
   (. .))


(S (NPA (PRP he))
   (VP (VBD died))
   (. !))


(S (NPA (NPPOS (NPP (NNP john))
               (POS 's))
        (NN daughter)
        (NPP (NNP mary)))
   (VP (VBD expressed)
       (NPA (NN sorrow)))
   (. .))


'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\nsections\n--------\n'),
])
def test_print_sections_for_communication(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--sections',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
Section 0 (0ab68635-c83d-4b02-b8c3-288626968e05), from 81 to 82:



Section 1 (54902d75-1841-4d8d-b4c5-390d4ef1a47a), from 85 to 162:

John Smith, manager of ACME INC, was bit by a dog on March 10th, 2013.
</P>


Section 2 (7ec8b7d9-6be0-4c62-af57-3c6c48bad711), from 165 to 180:

He died!
</P>


Section 3 (68da91a1-5beb-4129-943d-170c40c7d0f7), from 183 to 228:

John's daughter Mary expressed sorrow.
</P>



'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr


@mark.parametrize('args,output_prefix', [
    ((), ''),
    (('--annotation-headers',), '\nid\n--\n'),
])
def test_print_id_for_communication(comm_path, args, output_prefix):
    p = Popen([
        sys.executable, 'scripts/concrete_inspect.py',
        '--id',
    ] + list(args) + [
        comm_path
    ], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    expected_output = output_prefix + '''\
tests/testdata/serif_dog-bites-man.xml
'''
    assert 0 == p.returncode
    assert expected_output == stdout
    assert '' == stderr
